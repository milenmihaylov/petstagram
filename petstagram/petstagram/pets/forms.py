from django import forms

from petstagram.core.forms import BootstrapFormMixin
from petstagram.pets.models import Pet

PET_TYPE_CHOICES = [
	('dog', 'dog'),
	('cat', 'cat'),
	('parrot', 'parrot'),
]


class PetCreateForm(BootstrapFormMixin, forms.ModelForm):
	class Meta:
		model = Pet
		exclude = ('user',)
		# widgets = {
		# 	'type': forms.TextInput(
		# 		attrs={
		# 			'readonly': 'readonly',
		# 		}
		# 	)
		# }

