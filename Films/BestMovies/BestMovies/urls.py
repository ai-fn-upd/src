"""
URL configuration for BestMovies project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from BestMovies import settings

from BestMovies_api.views import (
    RegisterView,
    MovieListView,
    MovieDetailView,
    ProfileView,
    LikesView,
    AuthView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('register/', RegisterView.as_view()),
    path('movies/', MovieListView.as_view()),
    path('movies/<int:pk>/', MovieDetailView.as_view()),
    path('profile/', ProfileView.as_view()),
    path('likes/', LikesView.as_view()),
    path('login/', AuthView.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
