import uuid

from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


class CreateUpdateAbstractModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date Created")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Date Updated")

    class Meta:
        abstract = True


class Photo(CreateUpdateAbstractModel):
    image = models.ImageField(upload_to="photos", verbose_name='Photo')
    caption = models.CharField(max_length=200, verbose_name="Caption")
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="photos", verbose_name="Author")
    album = models.ForeignKey("webapp.Album", blank=True, null=True, on_delete=models.CASCADE, related_name="album_photos", verbose_name="Album")
    is_public = models.BooleanField(default=True, verbose_name="Is Public")
    favorite_users = models.ManyToManyField(get_user_model(), related_name="favorite_photos", blank=True, verbose_name="Favorite Users")
    token = models.UUIDField(default=uuid.uuid4, unique=True, null=True, blank=True)

    def __str__(self):
        return f"{self.pk} {self.author}"

    def get_absolute_url(self):
        return reverse("webapp:photo_view", kwargs={"pk": self.pk})

    class Meta:
        db_table = "photos"
        verbose_name = "Photo"
        verbose_name_plural = "Photos"