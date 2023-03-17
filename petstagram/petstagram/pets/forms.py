from django import forms

from petstagram.core.forms import BootstrapFormMixin
from petstagram.pets.models import Pet

PET_TYPE_CHOICES = [
	('dog', 'dog'),
	('cat', 'cat'),
	('parrot', 'parrot'),
]


class PetCreateForm(forms.ModelForm, BootstrapFormMixin):
	class Meta:
		model = Pet
		fields = '__all__'
		widgets = {
			'name': forms.TextInput(
				attrs={
					'class': 'some-class',
				},
			)
		}
