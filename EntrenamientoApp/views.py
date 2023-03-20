from django.views.generic import TemplateView, ListView, DetailView, UpdateView
#from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView 
#from django.contrib.auth.views import LoginView, PasswordChangeView
#from django.contrib.auth.forms import PasswordChangeForm
#from django.contrib.auth.mixins import LoginRequiredMixin
#from django.contrib.auth.models import User
#from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .models import Equipamiento

class HomeView(TemplateView):
    template_name = 'EntrenamientoApp/home.html'

# GYM

class GymLista(ListView):
    context_object_name = 'gyms'
    queryset = Equipamiento.objects.filter(equipamiento__startswith='gym')
    template_name = 'EntrenamientoApp/listaGym.html'
    #login_url = '/login/'

# FUNCIONAL

class FuncionalLista(ListView):
    context_object_name = 'funcionals'
    queryset = Equipamiento.objects.filter(equipamiento__startswith='funcional')
    template_name = 'EntrenamientoApp/listaFuncional.html'

# FUTBOL

class FutbolLista(ListView):
    context_object_name = 'futbols'
    queryset = Equipamiento.objects.filter(equipamiento__startswith='futbol')
    template_name = 'EntrenamientoApp/listaFutbol.html'

# BOXEO

class BoxeoLista(ListView):
    context_object_name = 'boxeos'
    queryset = Equipamiento.objects.filter(equipamiento__startswith='boxeo')
    template_name = 'EntrenamientoApp/listaBoxeo.html'

# BASQUET

class BasquetLista(ListView):
    context_object_name = 'basquets'
    queryset = Equipamiento.objects.filter(equipamiento__startswith='basquet')
    template_name = 'EntrenamientoApp/listaBasquet.html'

# OTRO

class OtroLista(ListView):
    context_object_name = 'otros'
    queryset = Equipamiento.objects.filter(equipamiento__startswith='otro')
    template_name = 'EntrenamientoApp/listaOtros.html'