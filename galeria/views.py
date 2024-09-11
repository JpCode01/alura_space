from django.shortcuts import render, get_object_or_404, redirect
from galeria.models import Fotografia
from django.contrib import messages

def index(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado!')
        return redirect('login')

    fotografia = Fotografia.objects.order_by("-data_fotografia").filter(publicado=True)

    return render(request, 'galeria/index.html', {"cards": fotografia})

def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html', {"fotografia": fotografia})

def buscar(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado!')
        return redirect('login')
    
    fotografia = Fotografia.objects.order_by("-data_fotografia").filter(publicado=True)

    if "buscar" in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            fotografia = fotografia.filter(nome__icontains=nome_a_buscar)

    return render(request, 'galeria/buscar.html', {"cards": fotografia})
