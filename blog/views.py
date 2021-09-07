from datetime import timezone
from django.shortcuts import render, get_object_or_404
from django.utils.timezone import now
from django.utils import timezone
# Create your views here.

from .models import Post

def publicacion_lista(request):
    publicaciones = Post.objects.filter (created_date__lte = timezone.now()).order_by('created_date')
    return render(request, 'blog/publicacion_lista.html', {'Publicaciones': Publicaciones})

def publicacion_detalle (request, pk):
    publicacion = get_object_or_404(Post, pk = pk)
    return render (request, 'blog/publicacion_detalle.html', {'publicacion': publicacion})

def pagina(request):
    return render(request, 'blog/pagina.html')
