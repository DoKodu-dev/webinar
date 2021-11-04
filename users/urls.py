from django.urls import path
from . import views

urlpatterns = [
    path('rejestracja', views.register, name='registration'),
    path('login', views.login, name='login'),
    path('panel', views.panel, name='panel'),
    path('save_vote', views.save_vote, name='save_vote')
]
