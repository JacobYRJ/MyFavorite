from django.conf.urls import url
from . import views

app_name = 'movie'

urlpatterns = [
	url(r'^movie', views.index, name = 'index'),
]