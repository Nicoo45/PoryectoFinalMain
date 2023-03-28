from django.views.generic import TemplateView, ListView, DetailView, UpdateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView 
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .models import Equipamiento, Comentario
from .forms import FormularioCambioPassword, FormularioEdicion, FormularioRegistroUsuario, FormularioNuevoEquipamiento, FormularioComentario, ActualizacionEquipamiento
from django.http import HttpResponse
#from django.conf import settings

#User = settings.AUTH_USER_MODEL

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
    login_url = '/login/'

class GymDetalle(LoginRequiredMixin, DetailView):
    model = Equipamiento
    context_object_name = 'gym'
    template_name = 'EntrenamientoApp/gymDetalle.html'

class GymUpdate(LoginRequiredMixin, UpdateView):
    model = Equipamiento
    form_class = ActualizacionEquipamiento
    success_url = reverse_lazy('gyms')
    context_object_name = 'gym'
    template_name = 'EntrenamientoApp/gymEdicion.html'

class GymDelete(LoginRequiredMixin, DeleteView):
    model = Equipamiento
    success_url = reverse_lazy('gyms')
    context_object_name = 'gym'
    template_name = 'Entrenamiento/gymBorrado.html'

# FUNCIONAL

class FuncionalLista(ListView):
    context_object_name = 'funcionals'
    queryset = Equipamiento.objects.filter(equipamiento__startswith='funcional')
    template_name = 'EntrenamientoApp/listaFuncional.html'

class FuncionalDetalle(LoginRequiredMixin,DetailView):
    model = Equipamiento
    context_object_name = 'funcional'
    template_name = 'EntrenamientoApp/funcionalDetalle.html'

class FuncionalUpdate(LoginRequiredMixin, UpdateView):
    model = Equipamiento
    form_class = ActualizacionEquipamiento
    success_url = reverse_lazy('funcionals')
    context_object_name = 'funcional'
    template_name = 'EntrenamientoApp/funcionalEdicion.html'

class FuncionalDelete(LoginRequiredMixin, DeleteView):
    model = Equipamiento
    success_url = reverse_lazy('funcionals')
    context_object_name = 'funcional'
    template_name = 'EntrenamientoApp/funcionalBorrado.html'

# FUTBOL

class FutbolLista(ListView):
    context_object_name = 'futbols'
    queryset = Equipamiento.objects.filter(equipamiento__startswith='futbol')
    template_name = 'EntrenamientoApp/listaFutbol.html'

class FutbolDetalle(LoginRequiredMixin,DetailView):
    model = Equipamiento
    context_object_name = 'futbol'
    template_name = 'EntrenamientoApp/futbolDetalle.html'

class FutbolUpdate(LoginRequiredMixin, UpdateView):
    model = Equipamiento
    form_class = ActualizacionEquipamiento
    success_url = reverse_lazy('futbols')
    context_object_name = 'futbol'
    template_name = 'EntrenamientoApp/futbolEdicion.html'

class FutbolDelete(LoginRequiredMixin, DeleteView):
    model = Equipamiento
    success_url = reverse_lazy('futbols')
    context_object_name = 'futbol'
    template_name = 'EntrenamientoApp/futbolBorrado.html'

# BOXEO

class BoxeoLista(ListView):
    context_object_name = 'boxeos'
    queryset = Equipamiento.objects.filter(equipamiento__startswith='boxeo')
    template_name = 'EntrenamientoApp/listaBoxeo.html'

class BoxeoDetalle(LoginRequiredMixin,DetailView):
    model = Equipamiento
    context_object_name = 'boxeo'
    template_name = 'EntrenamientoApp/boxeoDetalle.html'

class BoxeoUpdate(LoginRequiredMixin, UpdateView):
    model = Equipamiento
    form_class = ActualizacionEquipamiento
    success_url = reverse_lazy('boxeos')
    context_object_name = 'boxeo'
    template_name = 'EntrenamientoApp/boxeoEdicion.html'

class BoxeoDelete(LoginRequiredMixin, DeleteView):
    model = Equipamiento
    success_url = reverse_lazy('boxeos')
    context_object_name = 'boxeo'
    template_name = 'EntrenamientoApp/boxeoBorrado.html'

# BASQUET

class BasquetLista(ListView):
    context_object_name = 'basquets'
    queryset = Equipamiento.objects.filter(equipamiento__startswith='basquet')
    template_name = 'EntrenamientoApp/listaBasquet.html'

class BasquetDetalle(LoginRequiredMixin,DetailView):
    model = Equipamiento
    context_object_name = 'basquet'
    template_name = 'EntrenamientoApp/basquetDetalle.html'

class BasquetUpdate(LoginRequiredMixin, UpdateView):
    model = Equipamiento
    form_class = ActualizacionEquipamiento
    success_url = reverse_lazy('basquets')
    context_object_name = 'basquet'
    template_name = 'EntrenamientoApp/basquetEdicion.html'

class BasquetDelete(LoginRequiredMixin, DeleteView):
    model = Equipamiento
    success_url = reverse_lazy('basquets')
    context_object_name = 'basquet'
    template_name = 'EntrenamientoApp/basquetBorrado.html'

# OTRO

class OtroLista(ListView):
    context_object_name = 'otros'
    queryset = Equipamiento.objects.filter(equipamiento__startswith='otro')
    template_name = 'EntrenamientoApp/listaOtros.html'

class OtroDetalle(LoginRequiredMixin,DetailView):
    model = Equipamiento
    context_object_name = 'otro'
    template_name = 'EntrenamientoApp/otroDetalle.html'

class OtroUpdate(LoginRequiredMixin, UpdateView):
    model = Equipamiento
    form_class = ActualizacionEquipamiento
    success_url = reverse_lazy('otros')
    context_object_name = 'otro'
    template_name = 'EntrenamientoApp/otroEdicion.html'

class OtroDelete(LoginRequiredMixin, DeleteView):
    model = Equipamiento
    success_url = reverse_lazy('otros')
    context_object_name = 'otro'
    template_name = 'EntrenamientoApp/otroBorrado.html'

# CREACION INSTRUMENTO

class EquipamientoCreacion(LoginRequiredMixin, CreateView):
    model = Equipamiento
    form_class = FormularioNuevoEquipamiento
    success_url = reverse_lazy('home')
    template_name = 'EntrenamientoApp/equipamientoCreacion.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(EquipamientoCreacion, self).form_valid(form)

# COMENTARIOS

class ComentarioPagina(LoginRequiredMixin, CreateView):
    model = Comentario
    form_class = FormularioComentario
    template_name = 'EntrenamientoApp/comentario.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.comentario_id = self.kwargs['pk']
        return super(ComentarioPagina, self).form_valid(form)

# ACERCA DE MI

def about(request):
    return render(request, 'EntrenamientoApp/about.html', {})

def resultadosBusqueda(request):
    return render(request, "EntrenamientoApp/resultadosBusqueda.html")

def buscar(request):

    if request.GET["gym"]:    
        publicacion=request.GET["gym"] 
        equipamientos =Equipamiento.objects.filter(equipamiento__icontains=publicacion)

        return render(request, "EntrenamientoApp/resultadosBusqueda.html", {"equipamientos": equipamientos, "query":publicacion})

    else:

        mensaje= "No has introducido nada"

    return HttpResponse(mensaje)

def tiendas(request):
    return render(request, 'EntrenamientoApp/tiendas.html')

def carrusel(request):
    return render(request, 'EntrenamientoApp/carrusel.html')