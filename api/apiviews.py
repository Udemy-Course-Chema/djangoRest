# from rest_framework.views import APIView
# from rest_framework.response import Response
# from django.shortcuts import get_object_or_404

# ------- NUEVA VISTA GENÉRICA ----------
from rest_framework import generics

from .models import Product, Category, SubCategory
from .serializers import ProductSerializer, CategorySerializer, SubCategorySerializer

# class ProductList(APIView):
#     def get(self,request):
#         products = Product.objects.all()[:20]
#         data = ProductSerializer( products, many=True).data
#         return Response( data )
    
# class ProductDetail(APIView):
#     def get(self, request, pk):
#         product = get_object_or_404(Product, pk=pk)
#         data = ProductSerializer( product ).data
#         return Response( data )


# Crear un Product 
class ProductCreate( generics.CreateAPIView):
    serializer_class = ProductSerializer

class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetail(generics.RetrieveDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    

# Guardar una categoría
class CategorySave(generics.CreateAPIView):
    serializer_class = CategorySerializer

# Listar las categorías
class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# Detalles de una categoría    
class CategoryDetail(generics.RetrieveDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    

# Guardar una subcategoría
class SubCategorySave(generics.CreateAPIView):
    serializer_class = SubCategorySerializer


# Listar las subcategorías
class SubCategoryList(generics.ListCreateAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer
    

class SubCategoryListByCategory(generics.ListCreateAPIView):
    
    def get_queryset(self):
        queryset = SubCategory.objects.filter(category = self.kwargs["pk"] ) 
        return queryset
    serializer_class = SubCategorySerializer
    

# Detalle de una subcategoría
class SubCategoryDetail(generics.RetrieveDestroyAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer
    
