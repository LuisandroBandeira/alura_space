from django.shortcuts import get_object_or_404, render, redirect
from apps.galeria.models import Fotografia

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

