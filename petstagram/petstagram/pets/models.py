# from django.core.exceptions import ValidationError
from django.db import models


# def is_positive(value):
# 	if value<=0:
# 		raise ValidationError


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
		upload_to='images'
	)


class Like(models.Model):
	pet = models.ForeignKey(
		Pet,
		on_delete=models.CASCADE,
	)
