from django.shortcuts import render

from django.utils import timezone
# importe depuis les utilitaires de django "timezone" qui récupère la date et l'heure actuelle 
from .models import Post
# importe la table "Post" contenue dans models.py
from django.shortcuts import get_object_or_404
# récupère les contenus, si ils n'existent pas renvoi une 404
from .forms import PostForm
# importe la bibliothèque de formulaire
from django.shortcuts import redirect


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

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        # si la methode est égale à POST ( si on envoie du nouveau contenu)
        if form.is_valid():
            # si tous les champs sont remplis correctement
            post = form.save(commit=False)
            post.auteur = request.user
            post.published_date = timezone.now()
            post.save()
            # le formulaire est sauvegardé
            return redirect('post_detail', pk=post.pk)
            # renvoi le nouveau post à la page post_detail avec une valeur de clé
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_new.html', {'form': form})
    #renvoie au formulaire de création du blog concerné pour faire des modifs