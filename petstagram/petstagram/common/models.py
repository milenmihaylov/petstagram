from django.contrib.auth import get_user_model
from django.db import models

from petstagram.accounts.models import Account
from petstagram.pets.models import Pet

USER_MODEL = get_user_model()


class Comment(models.Model):
	comment = models.TextField()
	pet = models.ForeignKey(
		Pet,
		on_delete=models.CASCADE
	)
	user = models.ForeignKey(
		to=USER_MODEL,
		on_delete=models.CASCADE,
		null=True,
	)

	def __str__(self):
		return self.comment
