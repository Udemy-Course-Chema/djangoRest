from django.urls import path
from .views import categoria_list, categoria_details

urlpatterns = [
    path('categorias/', categoria_list, name="categoria_list"),
    path('categoria/detail/<int:pk>', categoria_details, name="categoria_details"),
]
