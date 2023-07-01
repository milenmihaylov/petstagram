from django.contrib.auth import login, logout
from django.shortcuts import render, redirect

from petstagram.petstagram_auth.forms import SignupUserForm, LoginUserForm


def signup_user(request):
	if request.method == 'POST':
		form = SignupUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request=request, user=user)
			return redirect('index')
	else:
		form = SignupUserForm()

	context = {
		'form': form,
	}
	return render(request, 'accounts/signup.html', context)


def login_user(request):
	if request.method == 'POST':
		form = LoginUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request=request, user=user)
			return redirect('index')
	else:
		form = LoginUserForm()

	context = {
		'form': form,
	}
	return render(request, 'accounts/login.html', context)


def logout_user(request):
	logout(request)
	return redirect('index')
