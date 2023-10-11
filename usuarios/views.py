from django.shortcuts import get_object_or_404, render

def login(request):
    # usuario = get_object_or_404(Usuario,pk=foto_id)
    return render(request,'usuarios/login.html')

def cadastro(request):
    return render(request,'usuarios/cadastro.html')