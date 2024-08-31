from django.contrib import admin
from webapp.models import Photo, Album

# Register your models here.
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'caption', 'album', 'is_public', 'created_at')
    list_filter = ('is_public', 'created_at')
    search_fields = ('caption', 'author__username', 'author__email')
    ordering = ('-created_at',)

admin.site.register(Photo, PhotoAdmin)

class AlbumAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'is_public', 'created_at')
    list_filter = ('is_public', 'created_at')
    search_fields = ('title', 'author__username', 'author__email')
    ordering = ('-created_at',)

admin.site.register(Album, AlbumAdmin)