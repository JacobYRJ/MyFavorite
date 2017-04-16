from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.models import User
import login



def index(request):
	if not request.user.is_authenticated():
		return redirect('login:login')
	else:
		
		return render(request, 'music/index.html')
