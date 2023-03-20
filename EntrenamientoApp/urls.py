from django import views
from django.urls import path
from .views import GymLista, HomeView, FuncionalLista, FutbolLista, BoxeoLista, BasquetLista, OtroLista
#from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
path('', HomeView.as_view(), name='home'),


    path('listaGym/', GymLista.as_view(), name='gyms'),
    path('listaFuncional/', FuncionalLista.as_view(), name='funcionals'),
    path('listaFutbol/', FutbolLista.as_view(), name='futbols'),
    path('listaBoxeo/', BoxeoLista.as_view(), name='boxeos'),
    path('listaBasquet/', BasquetLista.as_view(), name='basquets'),
    path('listaOtros/', OtroLista.as_view(), name='otros'),

]