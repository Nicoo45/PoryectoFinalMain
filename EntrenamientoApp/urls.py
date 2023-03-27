from django import views
from django.urls import path
from .views import GymLista, GymDetalle, HomeView, FuncionalLista, FuncionalDetalle, FuncionalUpdate, FuncionalDelete, FutbolDetalle, FutbolLista, FutbolUpdate, FutbolDelete, BoxeoLista, BoxeoDetalle, BoxeoUpdate, BoxeoDelete, BasquetLista, BasquetDetalle, BasquetUpdate, BasquetDelete, OtroLista, OtroDetalle, OtroUpdate, OtroDelete, LoginPagina, RegistroPagina, UsuarioEdicion, CambioPassword, EquipamientoCreacion, ComentarioPagina, GymUpdate, GymDelete, FuncionalDelete, FuncionalUpdate
from django.contrib.auth.views import LogoutView
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
path('', HomeView.as_view(), name='home'),

path('login/', LoginPagina.as_view(), name='login'),
path('logout/', LogoutView.as_view(template_name='EntrenamientoApp/logout.html'), name='logout'),
path('registro/', RegistroPagina.as_view(), name='registro'),
path('edicionPerfil/', UsuarioEdicion.as_view(), name='editar_perfil'),
path('passwordCambio/', CambioPassword.as_view(), name='cambiar_password'),
path('passwordExitoso/' , views.password_exitoso, name='password_exitoso'),

path('gymLista/', GymLista.as_view(), name='gyms'),
path('funcionalLista/', FuncionalLista.as_view(), name='funcionals'),
path('futbolLista/', FutbolLista.as_view(), name='futbols'),
path('boxeoLista/', BoxeoLista.as_view(), name='boxeos'),
path('basquetLista/', BasquetLista.as_view(), name='basquets'),
path('otroLista/', OtroLista.as_view(), name='otros'),

path('agregarEquipamiento/', EquipamientoCreacion.as_view(), name='nuevo'),

path('gymDetalle/<int:pk>', GymDetalle.as_view(), name='gym'),
path('funcionalDetalle/<int:pk>', FuncionalDetalle.as_view(), name='funcional'),
path('futbolDetalle/<int:pk>', FutbolDetalle.as_view(), name='futbol'),
path('boxeoDetalle/<int:pk>', BoxeoDetalle.as_view(), name='boxeo'),
path('basquetDetalle/<int:pk>', BasquetDetalle.as_view(), name='basquet'),
path('otroDetalle/<int:pk>', OtroDetalle.as_view(), name='otro'),

path('gymEdicion/<int:pk>/', GymUpdate.as_view(), name='gym_editar'),
path('funcionalEdicion/<int:pk>/', FuncionalUpdate.as_view(), name='funcional_editar'),
path('futbolEdicion/<int:pk>/', FutbolUpdate.as_view(), name='futbol_editar'),
path('boxeoEdicion/<int:pk>/', BoxeoUpdate.as_view(), name='boxeo_editar'),
path('basquetEdicion/<int:pk>/', BasquetUpdate.as_view(), name='basquet_editar'),
path('otroEdicion/<int:pk>/', OtroUpdate.as_view(), name='otro_editar'),

path('gymBorrado/<int:pk>/', GymDelete.as_view(), name='gym_eliminar'),
path('funcionalBorrado/<int:pk>/', FuncionalDelete.as_view(), name='funcional_eliminar'),
path('futbolBorrado/<int:pk>/', FutbolDelete.as_view(), name='futbol_eliminar'),
path('boxeoBorrado/<int:pk>/', BoxeoDelete.as_view(), name='boxeo_eliminar'),
path('basquetBorrado/<int:pk>/', BasquetDelete.as_view(), name='basquet_eliminar'),
path('otroBorrado/<int:pk>/', OtroDelete.as_view(), name='otro_eliminar'),

path('gymDetalle/<int:pk>/comentario/', ComentarioPagina.as_view(), name='comentario'),
path('funcionalDetalle/<int:pk>/comentario/', ComentarioPagina.as_view(), name='comentario'),
path('futbolDetalle/<int:pk>/comentario/', ComentarioPagina.as_view(), name='comentario'),
path('boxeoDetalle/<int:pk>/comentario/', ComentarioPagina.as_view(), name='comentario'),
path('basquetDetalle/<int:pk>/comentario/', ComentarioPagina.as_view(), name='comentario'),
path('otroDetalle/<int:pk>/comentario/', ComentarioPagina.as_view(), name='comentario'),

path('tiendas/', views.tiendas, name='tiendas'),
path('about/', views.about, name='about'),
path('buscar/', views.buscar),
path('carrusel/', views.carrusel, name='carrusel' )
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# y ahí le especifico a Django el directorio que voy a utilizar para subir
# ficheros.