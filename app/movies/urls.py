# app/movies/urls.py

from django.urls import path

from .views import MovieList, MovieDetail

from django.urls import reverse

urlpatterns = [
    path("movies/", MovieList.as_view(), name='movies'),
    path("movies/<int:pk>/", MovieDetail.as_view()),
]
