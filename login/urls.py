from django.conf.urls import url
from . import views


app_name = 'login'

urlpatterns = [
	url(r'^$', views.index, name='index'),
    url(r'^regist/$', views.UserFormView.as_view(), name='regist'),
    url(r'^login/$', views.user_login , name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
]