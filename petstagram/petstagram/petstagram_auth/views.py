from django.contrib.auth import login, logout
from django.contrib.auth.views import LogoutView, LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import View, TemplateView, FormView, CreateView

from petstagram.petstagram_auth.forms import SignupUserForm, LoginUserForm


# def signup_user(request):
# 	if request.method == 'POST':
# 		form = SignupUserForm(request.POST)
# 		if form.is_valid():
# 			user = form.save()
# 			login(request=request, user=user)
# 			return redirect('index')
# 	else:
# 		form = SignupUserForm()
#
# 	context = {
# 		'form': form,
# 	}
# 	return render(request, 'accounts/signup.html', context)


class SignUpUserView(CreateView):
	form_class = SignupUserForm
	template_name = 'accounts/signup.html'

	def form_valid(self, form):
		user = form.save()
		login(request=self.request, user=user)
		return redirect('account details')


# def login_user(request):
# 	if request.method == 'POST':
# 		form = LoginUserForm(request.POST)
# 		if form.is_valid():
# 			user = form.save()
# 			login(request=request, user=user)
# 			return redirect('index')
# 	else:
# 		form = LoginUserForm()
#
# 	context = {
# 		'form': form,
# 	}
# 	return render(request, 'accounts/login.html', context)


class LoginUserView(FormView):
	template_name = 'accounts/login.html'
	success_url = reverse_lazy('index')
	form_class = LoginUserForm

	def form_valid(self, form):
		user = form.save()
		login(self.request, user=user)
		return redirect('account details')


# def logout_user(request):
# 	logout(request)
# 	return redirect('index')


class LogoutUserView(LogoutView):
	next_page = reverse_lazy('index')
