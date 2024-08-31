from django import forms
from django.forms import widgets

from webapp.models import Album


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ["title", "description"]