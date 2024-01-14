from django.urls import path

from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView)
from . import views


urlpatterns = [
    path('register/', views.RegisterUserView.as_view()),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),

    path('categories/', views.AllCategoriesView.as_view(), name='all_categories'),
    path('product/all/', views.AllProductsView.as_view(), name='all_products'),
    path('product/category/<str:category>/', views.CategoryProductsView.as_view(), name='all_products_by_category'),
    path('product/id/<int:id_>/', views.ProductView.as_view(), name='get_product'),
    path('product/add/', views.AddProductView.as_view(), name='add_product'),
    # delete
    # add to cart
    # remove from cart
    # order -> popup plm
    # search
]
