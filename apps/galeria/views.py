import datetime
from django.shortcuts import get_object_or_404, render, redirect
from apps.galeria.models import Fotografia
from apps.galeria.forms import Fotografia, FotografiaForms
from django.contrib.auth.models import User
from django.contrib import auth, messages

def index(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    # Coloca-se um menos na frente do nome do campo para fazer order by desc
    fotografias = Fotografia.objects.order_by("-data_cadastro").filter(publicar=True)
    return render(request,'galeria/index.html', {"cards": fotografias})

def imagem(request, foto_id):
    # fotografia = Fotografia.objects.filter(id=foto_id).values()
    fotografia = get_object_or_404(Fotografia,pk=foto_id)
    return render(request,'galeria/imagem.html', {"fotografia":fotografia})

def buscar(request):
    if not request.user.is_authenticated:
        return redirect('login')

    fotografias = Fotografia.objects.order_by("-data_cadastro").filter(publicar=True)

    if "buscar" in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            fotografias = fotografias.filter(nome__icontains=nome_a_buscar)
            
    if "categoria" in request.GET:        
        nome_a_buscar = request.GET['categoria']
        if nome_a_buscar:
            fotografias = fotografias.filter(categoria__icontains=nome_a_buscar)
    return render(request,'galeria/buscar.html', {"cards":fotografias})

def nova_imagem(request):
    if not request.user.is_authenticated:
        messages.error(request,'Usuário não logado', 'alert-danger') 
        return redirect('login')
    form = FotografiaForms()
    if request.method == 'POST':
        # Para pegar as imagens da pagina tem usar request.FILES
        form = FotografiaForms(request.POST, request.FILES)
        if form.is_valid():
            form.data_cadastro = datetime.datetime.now()  
            form.save()
            return redirect('index')
    return render(request, 'galeria/nova_imagem.html', {'form': form})

def editar_imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia,id=foto_id)
    form = FotografiaForms(instance=fotografia)

    if request.method == 'POST':
        # Para pegar as imagens da pagina tem usar request.FILES, e passar a instância da fotografia
        form = FotografiaForms(request.POST, request.FILES, instance=fotografia)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'galeria/editar_imagem.html', {'form': form, 'foto_id': foto_id})

def deletar_imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia,id=foto_id)
    fotografia.delete()
    return redirect('index')

