from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from BestMovies_api.models import Movie


class MovieAdmin(admin.StackedInline):
    model = Movie


admin.site.register(Movie)
admin.site.site_header = "Фильмы"
admin.site.site_title = "Фильмы"
