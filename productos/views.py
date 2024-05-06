from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from productos.forms import ProductoForm
from .models import Producto 

# Create your views here.
def index(request):
  productos = Producto.objects.all().order_by('-id')
  data = {
    'productos': productos,
    'title': 'Listado de productos'
  }
  return render(request,'index.html',context=data)

def formulario(request):
  form = ProductoForm()
  context = {
    'form': form
    
  }
  if request.method == 'POST':
    form = ProductoForm(request.POST)
    if form.is_valid():
      form.save()
      context['mensaje'] = 'Producto guardado correctamente'
      return HttpResponseRedirect('/productos')
    else:
      context['mensaje'] = 'Error al guardar el producto'
  return render(request,'producto_form.html',context)
  
  

def detalle(request, producto_id):
  try:
    # producto = get_object_or_404(Producto, pk=producto_id)
    producto = Producto.objects.get(id=producto_id)
    data = {
      'producto': producto,
      'title': producto.nombre
    }
    return render(request,'detalle.html',context=data)
  except Producto.DoesNotExist:
    return render (request,'404.html')