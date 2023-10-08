from django.shortcuts import get_object_or_404, render
from galeria.models import Fotografia
def index(request):

    dados = {
        1: {"nome" : "Nebulosa de Carina",
            "legenda" : "webbtelescope.org | NASA | James Webb"},
        2: {"nome" : "Galáxia NGC 1079",
            "legenda" : "nasa.org | NASA | Hubble"}
    }
    # Coloca-se um menos na frente do nome do campo para fazer order by desc
    fotografias = Fotografia.objects.order_by("-data_cadastro").filter(publicar=True)
    return render(request,'galeria/index.html', {"cards": fotografias})

def imagem(request, foto_id):
    # fotografia = Fotografia.objects.filter(id=foto_id).values()
    fotografia = get_object_or_404(Fotografia,pk=foto_id)
    return render(request,'galeria/imagem.html', {"fotografia":fotografia})

