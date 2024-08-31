from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView

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

    def get_queryset(self):
        return Album.objects.filter(is_public=True)


class AlbumUpdateView(PermissionRequiredMixin, UpdateView):
    model = Album
    template_name = "albums/album_update.html"
    fields = ['title', 'description', 'is_public']
    permission_required = "webapp.change_album"

    def has_permission(self):
        return self.request.user == self.get_object().author or super().has_permission()

    def form_valid(self, form):
        return super().form_valid(form)

class AlbumDeleteView(PermissionRequiredMixin, DeleteView):
    model = Album
    template_name = "albums/album_confirm_delete.html"
    success_url = reverse_lazy('webapp:album_view')
    permission_required = "webapp.delete_album"

    def has_permission(self):
        return self.request.user == self.get_object().author or super().has_permission()

    def delete(self, request, *args, **kwargs):
        album = self.get_object()
        # Delete all photos in the album
        album.album_photos.all().delete()
        return super().delete(request, *args, **kwargs)