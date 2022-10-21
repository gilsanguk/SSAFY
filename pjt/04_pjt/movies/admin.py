from django.contrib import admin
from .models import Movie

class MovieAdmin (admin.ModelAdmin):
    list_diplay = ('id', 'title', 'audience', 'release_date', 'genre', 'score', 'poster_url', 'description')

# Register your models here.
admin.site.register(Movie, MovieAdmin)