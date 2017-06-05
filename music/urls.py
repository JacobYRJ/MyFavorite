from django.conf.urls import url
from . import views

app_name = 'music'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add_song/$', views.add_song, name='add_song'),
    url(r'^MySongs/$', views.detail, name='detail')
]
