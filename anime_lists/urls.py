"""urls для аниме листа"""

from django.urls import path
from . import views

app_name = 'anime_lists'
urlpatterns = [
    # home
    path('', views.index, name='index'),
    # title list
    path('titles/', views.titles, name='titles'),
    # information about some title
    path('titles/<int:title_id>/', views.title, name='title'),
]
