from django.urls import path
from apps.usuarios.views import login, cadastro, logout

urlpatterns = [
    path('logout', logout, name='logout'),
    path('login', login, name='login'),
    path('cadastro', cadastro, name='cadastro'),
]