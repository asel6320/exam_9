from django.urls import path

from webapp.views.photos import PhotosListView, PhotoCreateView, PhotoDetailView

app_name = "webapp"

urlpatterns = [
    path('', PhotosListView.as_view(), name="photos_list"),
    path('photos/create/', PhotoCreateView.as_view(), name="photo_create"),
    path('photo/<int:pk>/', PhotoDetailView.as_view(), name="photo_view"),
    # path('post/<int:pk>/update/', PostUpdateView.as_view(), name="post_update"),
    # path('post/<int:pk>/delete/', PostDeleteView.as_view(), name="post_delete"),
    # path('post/<int:pk>/like/', LikePostView.as_view(), name="post_like"),
]