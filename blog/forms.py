from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)
        #formulaire relié à base.html qui permet de poster des nouveaux contenus