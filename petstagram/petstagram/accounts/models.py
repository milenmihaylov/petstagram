from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models

USER_MODEL = get_user_model()


class Account(models.Model):
	name = models.CharField(
		max_length=30,
		blank=True,
	)
	email = models.EmailField(
		unique=True,
		blank=True,
		null=True,
	)
	picture = models.ImageField(
		upload_to='images/accounts',
		default='images/accounts/default/default_account_image.png',
		blank=True,
	)
	user = models.OneToOneField(
		to=USER_MODEL,
		on_delete=models.CASCADE,
		primary_key=True,
	)


from .signals import *
