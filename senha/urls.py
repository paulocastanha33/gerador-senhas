# senha/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.gerar_senha, name='gerar_senha'),
]
