from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


from rest_framework.permissions import IsAuthenticated, IsAdminUser

from .models import Component, Cpu, Gpu
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

        return Response(categories, status=status.HTTP_200_OK)


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

        data = Component.objects.get(category=category)
        products = [{
            'id': p.pk,
            'name': p.name,
            'price': p.price
        } for p in data]

        return Response(products, status=status.HTTP_200_OK)

class ProductView(APIView):
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


class AddProductView(APIView):
    permission_classes = [IsAdminUser]

    def post(self, request):
        category, data = request.data['category'], request.data['data']

        component = Component(
            name=data['name'],
            brand=data['brand'],
            series=data['series'],
            price=data['price'])
        component.save()
        if category == 'cpu':
            cpu = Cpu(
                component_fk=component,
                architecture=data['architecture'],
                cores=data['cores'],
                clock_speed=data['clockSpeed'])
            cpu.save()
        # if component:
        #     component.save()
        # else:
        #     return Response(status=status.HTTP_400_BAD_REQUEST)

        return Response(status=status.HTTP_201_CREATED)
