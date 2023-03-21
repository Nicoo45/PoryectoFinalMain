from django.views.generic import TemplateView, ListView, DetailView, UpdateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView 
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .models import Equipamiento
from .forms import FormularioCambioPassword, FormularioEdicion, FormularioRegistroUsuario


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'EntrenamientoApp/home.html'

class LoginPagina(LoginView):
    template_name = 'EntrenamientoApp/login.html'
    fields = '__all__'
    redirect_autheticated_user = True
    success_url = reverse_lazy('home')

    def get_success_url(self):
        return reverse_lazy('home')

class RegistroPagina(FormView):
    template_name = 'EntrenamientoApp/registro.html'
    form_class = FormularioRegistroUsuario
    redirect_autheticated_user = True
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegistroPagina, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('home')
        return super(RegistroPagina, self).get(*args, **kwargs)

class UsuarioEdicion(UpdateView):
    form_class = FormularioEdicion
    template_name= 'EntrenamientoApp/edicionPerfil.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user

class CambioPassword(PasswordChangeView):
    form_class = FormularioCambioPassword
    template_name = 'EntrenamientoApp/passwordCambio.html'
    success_url = reverse_lazy('password_exitoso')

def password_exitoso(request):
    return render(request, 'EntrenamientoApp/passwordExitoso.html', {})

# GYM

class GymLista(LoginRequiredMixin, ListView):
    context_object_name = 'gyms'
    queryset = Equipamiento.objects.filter(equipamiento__startswith='gym')
    template_name = 'EntrenamientoApp/listaGym.html'
    #login_url = '/login/'

class GymDetalle(DetailView):
    model = Equipamiento
    context_object_name = 'gym'
    template_name = 'EntrenamientoApp/gymDetalle.html'

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