from django.urls import path
from .views import home, RegisterView

urlpatterns = [
    path('', home, name='LoginRegisterSystem-home'),
    path('register/', RegisterView.as_view(), name='LoginRegisterSystem-register'),
]