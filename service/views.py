from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Categoria

# Create your views here.
def categoria_list(request):
    MAX_OBJECT = 20
    categories = Categoria.objects.all()[:MAX_OBJECT]
    data = { "result":list( categories.values("description", "active") ) }
    return JsonResponse( data )

def categoria_details(request, pk):
    categorie_detail = get_object_or_404(Categoria, pk=pk)
    data = {
        "result":{
            "description":categorie_detail.description,
            "active":categorie_detail.active
        }
    }
    
    return JsonResponse( data )
