from django.shortcuts import render
from django.views import generic
from django.contrib.auth.models import User

def index(request):
	username = request.POST.get('username')
	return render(request, 'music/index.html', {'username': username})
	