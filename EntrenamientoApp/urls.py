from django import views
from django.urls import path
from .views import GymLista, HomeView, FuncionalLista, FutbolLista, BoxeoLista, BasquetLista, OtroLista, LoginPagina, RegistroPagina, UsuarioEdicion, CambioPassword
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
path('', HomeView.as_view(), name='home'),

path('login/', LoginPagina.as_view(), name='login'),
path('logout/', LogoutView.as_view(template_name='EntrenamientoApp/logout.html'), name='logout'),
path('registro/', RegistroPagina.as_view(), name='registro'),
path('edicionPerfil/', UsuarioEdicion.as_view(), name='editar_perfil'),
path('passwordCambio/', CambioPassword.as_view(), name='cambiar_password'),
path('passwordExitoso/' , views.password_exitoso, name='password_exitoso'),

path('listaGym/', GymLista.as_view(), name='gyms'),
path('listaFuncional/', FuncionalLista.as_view(), name='funcionals'),
path('listaFutbol/', FutbolLista.as_view(), name='futbols'),
path('listaBoxeo/', BoxeoLista.as_view(), name='boxeos'),
path('listaBasquet/', BasquetLista.as_view(), name='basquets'),
path('listaOtros/', OtroLista.as_view(), name='otros'),

]