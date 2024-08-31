import uuid

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.forms import PhotoForm
from webapp.models import Photo


class PhotosListView(ListView):
    model = Photo
    template_name = "photos/photos_list.html"
    context_object_name = "photos"
    paginate_by = 3
    ordering = ("-created_at",)


class PhotoCreateView(LoginRequiredMixin, CreateView):
    form_class = PhotoForm
    template_name = "photos/photo_create.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PhotoDetailView(LoginRequiredMixin, DetailView):
    queryset = Photo.objects.all()
    template_name = "photos/photo_view.html"

    def get_queryset(self):
        return Photo.objects.filter(is_public=True)

class PhotoUpdateView(PermissionRequiredMixin, UpdateView):
    model = Photo
    form_class = PhotoForm
    template_name = "photos/photo_update.html"
    permission_required = "webapp.change_photo"

    def has_permission(self):
        return self.request.user == self.get_object().author or super().has_permission()


class PhotoDeleteView(PermissionRequiredMixin, DeleteView):
    model = Photo
    template_name = "photos/photo_delete.html"
    permission_required = "webapp.delete_photo"

    def has_permission(self):
        return self.request.user == self.get_object().author or super().has_permission()

    def get_success_url(self):
        return reverse('webapp:photos_list')


class GenerateTokenView(View):
    def post(self, request, pk):
        photo = get_object_or_404(Photo, pk=pk)

        if request.user == photo.author:
            if not photo.token:
                photo.token = uuid.uuid4()
                photo.save()

        return redirect('webapp:photo_detail', pk=pk)

class TokenPhotoDetailView(View):
    def get(self, request, token):
        photo = get_object_or_404(Photo, token=token)
        return render(request, 'photos/photo_view.html', {'photo': photo})