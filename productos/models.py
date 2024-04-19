from django.db import models
from django.utils import timezone
# Create your models here.
class Categoria(models.Model):
  nombre = models.CharField(max_length=255)
  
  def __str__(self):
    return self.nombre
  
class Producto(models.Model):
  nombre = models.CharField(max_length=255)
  stock = models.IntegerField()
  puntaje = models.FloatField()
  categoria = models.ForeignKey(
    Categoria,
    on_delete=models.CASCADE
    )
  #CASCADE: elimina el produto
  #PROTECT: no se puede eliminar la categoria lanza error
  #RESTRICT: solo elimina si no existe productos
  #SET_NULL: pone la categoria en null
  #SET_DEFAULT: pone la categoria en un valor por defecto
  creado_en = models.DateTimeField(default=timezone.now)
  
  def __str__(self) -> str:
    return self.nombre