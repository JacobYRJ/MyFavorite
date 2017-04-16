from django.shortcuts import render, redirect
from django.views import View, generic
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import UserForm
import music


def index(request):
	if not request.user.is_authenticated():
		return redirect('login:login')
	else:
		return redirect('music:index')
	
	
	
class UserFormView(View):
	form_class = UserForm
	template_name = 'login/register.html'
	
	def get(self, request):
		form = self.form_class
		return render(request, self.template_name, {'form': form})
	
	def post(self, request):
		form = self.form_class(request.POST or None)
		
		if form.is_valid():
			user = form.save(commit=False)
			
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user.set_password(password)
			user.save()
			
			user = authenticate(username=username, password=password)
			
			if user is not None:
				
				if user.is_active:
					login(request, user)
					return redirect('login:index')
			return render(request, self.template_name, {'form': form})
		
		
def user_login(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('login:index')
		else:
			return render(request, 'login/login.html', {'error_message': 'You have an error'})
		return render(request, 'login/login.html')
	return render(request, 'login/login.html')


def user_logout(request):
	logout(request)
	return redirect('login:login')