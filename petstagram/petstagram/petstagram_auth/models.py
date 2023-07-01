from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from petstagram.petstagram_auth.managers import PetstagramUserManager


class PetstagramUser(AbstractBaseUser, PermissionsMixin):
	username_validator = UnicodeUsernameValidator()

	username = models.CharField(
		_('username'),
		max_length=150,
		unique=True,
		help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
		validators=[username_validator],
		error_messages={
			'unique': _("A user with that username already exists."),
		},
	)

	is_staff = models.BooleanField(
		_('staff status'),
		default=False,
		help_text=_('Designates whether the user can log into this admin site.'),
	)

	objects = PetstagramUserManager()

	USERNAME_FIELD = 'username'

	date_joined = models.DateTimeField(
		auto_now_add=True,
	)
