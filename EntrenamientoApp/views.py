from django.shortcuts import render

def home(request):
    return render(request, 'EntrenamientoApp/home.html')

def servicios(request):
    return render(request, 'EntrenamientoApp/servicios.html')

def tienda(request):
    return render(request, 'EntrenamientoApp/tienda.html')

def blog(request):
    return render(request, 'EntrenamientoApp/blog.html')

def contacto(request):
    return render(request, 'EntrenamientoApp/contacto.html')