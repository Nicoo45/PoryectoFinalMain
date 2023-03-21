from django import views
from django.urls import path, include
from .views import GymLista, HomeView, FuncionalLista, FutbolLista, BoxeoLista, BasquetLista, OtroLista, GymDetalle
#from django.contrib.auth.views import LogoutView
from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views
from LoginRegisterSystem.views import CustomLoginView
from LoginRegisterSystem.forms import LoginForm

urlpatterns = [
path('', HomeView.as_view(), name='home'),

path('', include('LoginRegisterSystem.urls')),
    path('login/', CustomLoginView.as_view(redirect_authenticated_user=True, template_name='LoginRegisterSystem/login.html',
                                           authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='LoginRegisterSystem/logout.html'), name='logout'),

path('listaGym/', GymLista.as_view(), name='gyms'),
path('listaFuncional/', FuncionalLista.as_view(), name='funcionals'),
path('listaFutbol/', FutbolLista.as_view(), name='futbols'),
path('listaBoxeo/', BoxeoLista.as_view(), name='boxeos'),
path('listaBasquet/', BasquetLista.as_view(), name='basquets'),
path('listaOtros/', OtroLista.as_view(), name='otros'),
    
path('gymDetalle/<int:pk>/', GymDetalle.as_view(), name='gym'),
#path('funcionalDetalle/<int:pk>/', FuncionalDetalle.as_view(), name='funcional'),
#path('futbolDetalle/<int:pk>/', FutbolDetalle.as_view(), name='futbol'),
#path('boxeoDetalle/<int:pk>/', BoxeoDetalle.as_view(), name='boxeo'),
#path('basquetDetalle/<int:pk>/', BasquetDetalle.as_view(), name='basquet'),
#path('otroDetalle/<int:pk>/', OtroDetalle.as_view(), name='otro'),
]