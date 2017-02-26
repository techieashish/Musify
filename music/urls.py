__author__ = 'ASHISH'
from django.conf.urls import url
from . import views

app_name = 'music'


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/', views.user_login, name='login'),
    url(r'^logout/', views.user_logout, name='logout'),
    url(r'^register/', views.user_registration, name='register'),
    url(r'^dash/', views.dash, name='dash'),
    url(r'^create/', views.create_profile, name='create'),
    url(r'^(?P<album_id>[0-9]+)/album/$', views.album, name='album'),
    url(r'^albums/$', views.albums, name='albums'),
    url(r'^songs/$', views.songs, name='songs'),
    url(r'^editprofile/$', views.edit_profile, name='pedit'),
    url(r'^(?P<album_id>[0-9]+)/(?P<song_id>[0-9]+)/editsong/$', views.edit_song, name='sedit'),
    url(r'^(?P<album_id>[0-9]+)/editalbum/$', views.edit_album, name='aedit'),
    url(r'^(?P<album_id>[0-9]+)/deletealbum/$', views.album_delete, name='adelete'),
    url(r'^(?P<album_id>[0-9]+)/(?P<song_id>[0-9]+)/deletesong/$', views.song_delete, name='sdelete'),
    url(r'^(?P<album_id>[0-9]+)/add_song/$', views.add_song, name='add_song'),
    url(r'^add-album/$', views.add_album, name='add_album'),
]