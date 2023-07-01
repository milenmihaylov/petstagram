from django import forms
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.forms import UserCreationForm, UsernameField, AuthenticationForm
from django.core.exceptions import ValidationError

USER_MODEL = get_user_model()


class SignupUserForm(UserCreationForm):
	class Meta:
		model = USER_MODEL
		fields = ("username",)
		field_classes = {'username': UsernameField}


class LoginUserForm(forms.Form):
	username = forms.CharField(
		max_length=20,
	)
	password = forms.CharField(
		widget=forms.PasswordInput,
	)
	user = None

	def clean_password(self):
		self.user = authenticate(
			username=self.cleaned_data['username'],
			password=self.cleaned_data['password'],
		)
		if not self.user:
			raise ValidationError('Username and/or password invalid!')

	def save(self):
		return self.user
