from django.urls import path 
from api.apiviews import ProductList, ProductDetail

urlpatterns = [
    path('v1/products/', ProductList.as_view(), name='product_list' ), 
    path('v1/product/<int:pk>', ProductDetail.as_view(), name='product_detail'),
]
