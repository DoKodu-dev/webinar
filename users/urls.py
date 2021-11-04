from django.urls import path
from . import views

urlpatterns = [
    path('rejestracja', views.register, name='registration'),
    path('login', views.login, name='login'),
    path('panel', views.panel, name='panel'),
]
