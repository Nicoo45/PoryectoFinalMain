from django.db import models
import os
from django.conf import settings
from django.contrib.auth.models import User
#from PIL import Image
#from django.db.models.signals import post_save

class Equipamiento(models.Model):
    equipamientoSeleccion = (
    ('gym','GYM'),
    ('funcional', 'FUNCIONAL'),
    ('futbol','FUTBOL'),
    ('boxeo','BOXEO'),
    ('basquet','BASQUET'),
    ('otro', 'Otro'),
    )
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    titulo = models.CharField(max_length=200)
    equipamiento = models.CharField(max_length=15, choices=equipamientoSeleccion, default='gym')
    marca = models.CharField(max_length=40)
    descripcion = models.TextField(null=True, blank=True)
    year = models.IntegerField() 
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    usado = models.BooleanField()
    fechaPublicacion = models.DateTimeField(auto_now_add=True)
    telefonoContacto = models.IntegerField()
    emailContacto = models.EmailField()
    imagenEquipamiento = models.ImageField(null=True, blank=True, upload_to="imagenes/")

    class Meta:
        ordering = ['usuario', '-fechaPublicacion']

    def __str__(self):
        return self.titulo
    
class Comentario(models.Model):
    comentario = models.ForeignKey(Equipamiento, related_name='comentarios', on_delete=models.CASCADE, null=True)
    nombre = models.CharField(max_length=40)
    mensaje = models.TextField(null=True, blank=True)
    fechaComentario = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-fechaComentario']

    def __str__(self):
        return '%s - %s' % (self.nombre, self.comentario)