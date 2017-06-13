from django.conf.urls import url
from . import views

app_name = 'music'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add_song/$', views.add_song, name='add_song'),
    url(r'^MySongs/$', views.detail, name='detail'),
    url(r'^MySongs/(?P<song_id>[0-9]+)/$', views.favorite, name='favorite'),
    url(r'^MySongs/(?P<song_id>[0-9]+)/delete_song/$', views.delete_song, name='delete_song'),
]
