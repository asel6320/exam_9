from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
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

