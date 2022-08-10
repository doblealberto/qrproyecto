"""Post forms."""

# Django
from django import forms

# Models
from posts.models import Post, Mausoleo


class PostForm(forms.ModelForm):
    """Post model form."""

    class Meta:
        """Form settings."""

        model = Post
        fields = ('user', 'profile', 'title', 'photo')


class MausoleoForm(forms.ModelForm):
    """Post model form."""

    class Meta:
        """Form settings."""

        model = Mausoleo
        fields = ('nombre', 'descripcion', 'photo')
