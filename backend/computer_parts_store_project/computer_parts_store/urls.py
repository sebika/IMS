from django.urls import path

from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView)
from . import views


urlpatterns = [
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),

    path('register/', views.RegisterUserView.as_view()),
    path('categories/', views.AllCategoriesView.as_view(), name='all_categories'),
    path('product/all/', views.AllProductsView.as_view(), name='all_products'),
    path('product/category/<str:category>/', views.CategoryProductsView.as_view(), name='all_products_by_category'),
    path('product/id/<int:id_>/', views.GetProductView.as_view(), name='get_product'), # at this url you can get a product by id
    path('product/delete/<int:id_>/', views.DeleteProductView.as_view(), name='delete_product'), # at this url you can delete a product by id
    path('product/add/', views.AddProductView.as_view(), name='add_product'),
    path('cart/all/', views.AllCartProductsView.as_view(), name='all_cart_items'),
    path('cart/add/', views.AddToCartView.as_view(), name='add_to_cart'),
    # remove from cart
    path('cart/delete/<int:id_>/', views.DeleteFromCartView.as_view(), name='delete_from_cart'),
    # order
    path('cart/checkout/', views.CheckoutView.as_view(), name='checkout'),
    # path('orders/all/', views.AllOrdersView.as_view(), name='all_orders'),
]
