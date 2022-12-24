from django.urls import path 
from api.apiviews import ProductCreate,ProductList,ProductDetail,\
        CategorySave,CategoryList, CategoryDetail,\
        SubCategorySave,SubCategoryList, SubCategoryDetail, SubCategoryListByCategory 

urlpatterns = [
    # Productos
    path('v1/product/create/', ProductCreate.as_view(), name='product_create' ),
    path('v1/products/', ProductList.as_view(), name='products_list' ), 
    path('v1/product/<int:pk>/', ProductDetail.as_view(), name='product_detail'),
    # Categorias
    path('v2/category/create/', CategorySave.as_view(), name='create_category'),
    path('v2/categories/', CategoryList.as_view(), name='categories_list'),
    path('v2/category/<int:pk>/', CategoryDetail.as_view(), name='category_detail'),
    # SubCategorias
    path('v2/subcategory/create/', SubCategorySave.as_view(), name='create_subcategory'),
    path('v2/subcategories/', SubCategoryList.as_view(), name='subcategories_list'),
    path('v2/subcategory/<int:pk>/', SubCategoryDetail.as_view(), name='subcategories_list'),
    # Categorías con sus Subcategorías
    # path('v3/category/<int:pk>/subcategories/'),
    # path('v3/category/<int:pk>/subcategory/<int:pk>'),
    
    # SubCategorías por Categorías
    path('v3/category/<int:pk>/subcategories', SubCategoryListByCategory.as_view(), name='subcategories_by_category'),
]
