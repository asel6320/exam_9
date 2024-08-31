from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
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
    model = Album
    template_name = "albums/album_view.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        album = self.object

        photos = album.album_photos.filter(is_public=True).order_by('-created_at')

        paginator = Paginator(photos, 10)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context['photos'] = page_obj
        context['album'] = album
        return context


class AlbumUpdateView(LoginRequiredMixin, UpdateView):
    model = Album
    template_name = "albums/album_update.html"
    fields = ['title', 'description', 'is_public']

    def form_valid(self, form):
        return super().form_valid(form)

class AlbumDeleteView(LoginRequiredMixin, DeleteView):
    model = Album
    template_name = "albums/album_confirm_delete.html"
    success_url = reverse_lazy('webapp:album_view')

    def delete(self, request, *args, **kwargs):
        album = self.get_object()
        # Delete all photos in the album
        album.album_photos.all().delete()
        return super().delete(request, *args, **kwargs)