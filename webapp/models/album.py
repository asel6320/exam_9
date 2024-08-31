from django.db import models
from django.contrib.auth import get_user_model

from webapp.models import CreateUpdateAbstractModel


class Album(CreateUpdateAbstractModel):
    title = models.CharField(max_length=255, verbose_name='Title')
    description = models.TextField(max_length=2000, blank=True, null=True, verbose_name='Description')
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="albums", verbose_name="Author")

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'albums'
        verbose_name = 'Album'
        verbose_name_plural = 'Albums'