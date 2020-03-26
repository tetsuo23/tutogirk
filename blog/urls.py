from django.urls import path
from . import views

# path ("URL, nom de la vue dans VIEWS.PY,  nom de ...?")
urlpatterns = [

    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    # chemin vers le formulaire de post de nouveau contenu
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    # chemin vers le formulaire d'édition de contenu
]

    


