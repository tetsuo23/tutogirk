from django.shortcuts import render

from django.utils import timezone
# importe depuis les utilitaires de django "timezone" qui récupère la date et l'heure actuelle 
from .models import Post
# importe la table "Post" contenue dans models.py
from django.shortcuts import get_object_or_404
# récupère les contenus, si ils n'existent pas renvoi une 404


def post_list(request):

    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    # attribue à la variable "posts" les objets Post triés par date de publication 
    return render(request, 'blog/post_list.html', {'posts': posts})
    # entre {} , 'nom de l'information envoyée au template' : nom de la variable


def base(request):
    return render(request, 'blog/base.html', {})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})