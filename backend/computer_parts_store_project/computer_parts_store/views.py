from typing import Any, Dict, List
from django.contrib.auth import get_user_model
from django.shortcuts import redirect
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
import os
import requests

from .models import CartProduct, Component, Cpu, Gpu, Order, OrderProduct
from .serializers import UserSerializer

CustomUser = get_user_model()


class RegisterUserView(APIView):
    def post(self, request):
        # if email is already in use
        if CustomUser.objects.filter(email=request.data['email']).exists():
            return Response({'error': 'Email already registered'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AllCategoriesView(APIView):
    def get(self, request):
        categories = Component.objects.values_list('category', flat=True).distinct()
        categories = [cat.upper() for cat in categories]

        return Response(categories, status=status.HTTP_200_OK, headers={'Access-Control-Allow-Origin': '*'})


class AllProductsView(APIView):
    def get(self, request):
        data = Component.objects.all()
        products = [{
            'id': p.pk,
            'name': p.name,
            'price': p.price
        } for p in data]

        return Response(products, status=status.HTTP_200_OK)


class CategoryProductsView(APIView):
    def get(self, request, *args, **kwargs):
        category = kwargs['category']
        print(category)

        data = Component.objects.filter(category=category)
        products = [{
            'id': p.pk,
            'name': p.name,
            'price': p.price
        } for p in data]

        return Response(products, status=status.HTTP_200_OK)

class GetProductView(APIView):
    def get(self, request, *args, **kwargs):
        id_ = kwargs['id_']

        data = Component.objects.get(pk=id_)
        product = {
            'id': data.pk,
            'name': data.name,
            'brand': data.brand,
            'series': data.series,
            'price': data.price,
            'category': data.category
        }

        if data.category == 'cpu':
            additional_data = Cpu.objects.get(component_fk_id=id_)
            product['architecture'] = additional_data.architecture
            product['cores'] = additional_data.cores
            product['clock_speed'] = additional_data.clock_speed
        if data.category == 'gpu':
            additional_data = Gpu.objects.get(component_fk_id=id_)
            product['memory_capacity'] = additional_data.memory_capacity
            product['memory_type'] = additional_data.memory_type
            product['clock_speed'] = additional_data.clock_speed

        return Response(product, status=status.HTTP_200_OK)


class DeleteProductView(APIView):
    permission_classes = [IsAdminUser]

    def delete(self, request, *args, **kwargs):
        id_ = kwargs['id_']

        component = Component.objects.get(pk=id_)
        if not component:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        component.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class AddProductView(APIView):
    permission_classes = [IsAdminUser]

    def post(self, request):
        category, data = request.data['category'], request.data['data']

        response = requests.post(f'{os.getenv("PAYMENT_API")}/add_item', json={
            'name': data['name'],
            'price': data['price']
        })

        component = Component(
            name=data['name'],
            brand=data['brand'],
            series=data['series'],
            price=data['price'],
            price_id=response.json()['price_id'],
            category=category,
        )
        component.save()

        if category == 'cpu':
            Cpu(
                component_fk=component,
                architecture=data['architecture'],
                cores=data['cores'],
                clock_speed=data['clockSpeed']
            ).save()

        elif category == 'gpu':
            Gpu(
                component_fk=component,
                memory_capacity=data['memory_capacity'],
                memory_type=data['memory_type'],
                clock_speed=data['clock_speed']
            ).save()

        return Response(status=status.HTTP_201_CREATED)


class AllCartProductsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        cartProducts = CartProduct.objects.all()
        components = []
        quantities = []
        cart_products_ids = []
        for cp in cartProducts:
            components.append(Component.objects.get(pk=cp.component_id))
            quantities.append(cp.quantity)
            cart_products_ids.append(cp.pk)

        components = [{
            'id': p.pk,
            'name': p.name,
            'price': p.price,
            'quantity': q,
            'cart_product_id': cp_id
        } for p, q, cp_id in zip(components, quantities, cart_products_ids)]

        return Response(components, status=status.HTTP_200_OK)

class AddToCartView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        CartProduct(
            user_id=request.user.pk,
            component_id=request.data['product_id'],
            quantity=request.data['quantity']
        ).save()
        return Response(status=status.HTTP_200_OK)

class DeleteFromCartView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        id_ = kwargs['id_']

        cart_product = CartProduct.objects.get(pk=id_)
        if not cart_product:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        cart_product.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

# This test secret API key is a placeholder. Don't include personal details in requests with this key.
# To see your test secret API key embedded in code samples, sign in to your Stripe account.
# You can also find your test secret API key at https://dashboard.stripe.com/test/apikeys.


class CheckoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = CustomUser.objects.get(pk=request.user.pk)
        order = Order(
            user=user,
            shipping_address=request.data['address'],
            phone=request.data['phone']
        )

        cartProducts = CartProduct.objects.filter(user=user)
        if not cartProducts:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        line_items: List[Any] = []
        order.save()
        for cp in cartProducts:
            OrderProduct(
                order=order,
                component=cp.component,
                quantity=cp.quantity
            ).save()

            line_items.append({
                'price': cp.component.price_id,
                'quantity': cp.quantity,
            })

            cp.delete()

        response = requests.post(f'{os.getenv("PAYMENT_API")}/create-checkout-session', json={ 'line_items': line_items })

        return Response({'url': response.json()['url']}, status=200)

class AllOrdersView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = CustomUser.objects.get(pk=request.user.pk)
        if user.is_staff:
            orders = Order.objects.all()
        else:
            orders = Order.objects.filter(user=user)
        orders = [{
            'id': o.pk,
            'shipping_address': o.shipping_address,
            'phone': o.phone,
            'date': o.date_ordered.strftime("%Y-%m-%d %H:%M"),
            'products': [{
                'name': op.component.name,
                'price': op.component.price,
                'quantity': op.quantity
            } for op in OrderProduct.objects.filter(order=o)]
        } for o in orders]

        return Response(orders, status=status.HTTP_200_OK)

class DeleteOrderView(APIView):
    permission_classes = [IsAdminUser]

    def delete(self, request, *args, **kwargs):
        id_ = kwargs['id_']
        print(id_)
        order = Order.objects.get(pk=id_)
        print(order)
        if not order:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        order.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
