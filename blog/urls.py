from django.urls import path
from . import views

# path ("URL, nom de la vue dans VIEWS.PY,  nom de ...?")
urlpatterns = [
    path('post', views.post_list, name='post_list'),
    path('', views.base),
]