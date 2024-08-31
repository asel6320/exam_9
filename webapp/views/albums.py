from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.forms import AlbumForm
from webapp.models import Album


class AlbumCreateView(LoginRequiredMixin, CreateView):
    form_class = AlbumForm
    template_name = "albums/album_create.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class AlbumDetailView(LoginRequiredMixin, DetailView):
    queryset = Album.objects.all()
    template_name = "albums/album_view.html"