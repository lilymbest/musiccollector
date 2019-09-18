from django.urls import path, include
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('mymusic/', views.mymusic, name='music'),
  path('discover/', views.discover, name='discover'),
  path('mymusic/new', views.new, name='new'),
  path('mymusic/playlists', views.playlists, name='playlists'),
  path('mymusic/favorite_tracks', views.favorite_tracks, name="favorite_tracks"),
  path('mymusic/<int:song_id>/', views.detail, name='details'),
  path('accounts/profile/', views.profile, name='profile'),
  path('accounts/signup/', views.signup, name='signup'),
]

