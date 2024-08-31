from django.urls import path

from webapp.views.photos import PhotosListView, PhotoCreateView, PhotoDetailView, PhotoUpdateView, PhotoDeleteView
from webapp.views.albums import AlbumDetailView, AlbumCreateView

app_name = "webapp"

urlpatterns = [
    path('', PhotosListView.as_view(), name="photos_list"),
    path('photos/create/', PhotoCreateView.as_view(), name="photo_create"),
    path('photo/<int:pk>/', PhotoDetailView.as_view(), name="photo_view"),
    path('photo/<int:pk>/update/', PhotoUpdateView.as_view(), name="photo_update"),
    path('photo/<int:pk>/delete/', PhotoDeleteView.as_view(), name="photo_delete"),
    path('albums/create/', AlbumCreateView.as_view(), name="album_create"),
    path('album/<int:pk>/', AlbumDetailView.as_view(), name="album_view"),
    #path('post/<int:pk>/like/', LikePostView.as_view(), name="post_like"),
]