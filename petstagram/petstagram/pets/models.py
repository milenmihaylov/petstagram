# from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from django.db import models

from petstagram.accounts.models import Account


# def is_positive(value):
# 	if value<=0:
# 		raise ValidationError

USER_MODEL = get_user_model()


class Pet(models.Model):
	TYPE_CHOICE_DOG = 'dog'
	TYPE_CHOICE_CAT = 'cat'
	TYPE_CHOICE_PARROT = 'parrot'
	TYPE_CHOICE_SNAKE = 'snake'
	TYPE_CHOICE_RABBIT = 'rabbit'

	TYPE_CHOICES = (
		(TYPE_CHOICE_DOG, 'Dog'),
		(TYPE_CHOICE_CAT, 'Cat'),
		(TYPE_CHOICE_PARROT, 'Parrot'),
		(TYPE_CHOICE_SNAKE, 'Snake'),
		(TYPE_CHOICE_RABBIT, 'Rabbit'),
	)
	type = models.CharField(
		max_length=6,
		choices=TYPE_CHOICES,
	)
	name = models.CharField(
		max_length=6,
	)
	age = models.PositiveIntegerField()
	# validators=[
	# 	is_positive,
	# ]

	description = models.TextField()
	image = models.ImageField(
		upload_to='images/pets'
	)

	user = models.ForeignKey(
		to=USER_MODEL,
		on_delete=models.CASCADE,
		null=True,
	)

	def delete(self, **kwargs):
		self.image.delete()
		super().delete(**kwargs)


class Like(models.Model):
	pet = models.ForeignKey(
		Pet,
		on_delete=models.CASCADE,
	)
	user = models.ForeignKey(
		to=USER_MODEL,
		on_delete=models.CASCADE,
		null=True,
	)
