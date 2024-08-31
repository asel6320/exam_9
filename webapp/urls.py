from django.urls import path

from webapp.views.photos import (PhotosListView, PhotoCreateView, PhotoDetailView, PhotoUpdateView,
                                 PhotoDeleteView, GenerateTokenView, TokenPhotoDetailView)
from webapp.views.albums import AlbumDetailView, AlbumCreateView, AlbumUpdateView, AlbumDeleteView
from webapp.api import add_to_favorites, remove_from_favorites
app_name = "webapp"

urlpatterns = [
    path('', PhotosListView.as_view(), name="photos_list"),
    path('photos/create/', PhotoCreateView.as_view(), name="photo_create"),
    path('photo/<int:pk>/', PhotoDetailView.as_view(), name="photo_view"),
    path('photo/<int:pk>/update/', PhotoUpdateView.as_view(), name="photo_update"),
    path('photo/<int:pk>/delete/', PhotoDeleteView.as_view(), name="photo_delete"),
    path('albums/create/', AlbumCreateView.as_view(), name="album_create"),
    path('album/<int:pk>/', AlbumDetailView.as_view(), name="album_view"),
    path('album/<int:pk>/update/', AlbumUpdateView.as_view(), name="album_update"),
    path('album/<int:pk>/delete/', AlbumDeleteView.as_view(), name="album_delete"),
    path('api/favorites/add/<str:item_type>/<int:item_id>/', add_to_favorites, name='add_to_favorites'),
    path('api/favorites/remove/<str:item_type>/<int:item_id>/', remove_from_favorites, name='remove_from_favorites'),
    path('photos/<int:pk>/generate-token/', GenerateTokenView.as_view(), name='generate_token'),
    path('photos/token/<uuid:token>/', TokenPhotoDetailView.as_view(), name='token_photo_detail'),
]