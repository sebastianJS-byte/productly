from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Producto 

# Create your views here.
def index(request):
  productos = Producto.objects.all().order_by('-id').values()
  productos = list(productos)
  
  # productosPuntaje = Producto.objects.filter(puntaje=3)
  # productosGet = Producto.objects.get(id=1)
  data = {
    'productos': productos,
    'count': len(productos),
    'title': 'Listado de productos'
  }
  print("Data: ", data)
  return JsonResponse(data, safe=False)