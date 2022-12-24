from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import Product
from .serializers import ProductSerializer

class ProductList(APIView):
    def get(self,request):
        products = Product.objects.all()[:20]
        data = ProductSerializer( products, many=True).data
        return Response( data )
    
class ProductDetail(APIView):
    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        data = ProductSerializer( product ).data
        return Response( data )
    
