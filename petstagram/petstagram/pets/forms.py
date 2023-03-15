from django import forms

from petstagram.pets.models import Pet

PET_TYPE_CHOICES = [
	('dog', 'dog'),
	('cat', 'cat'),
	('parrot', 'parrot'),
]


class PetCreateForm(forms.ModelForm):
	type = forms.ChoiceField(
		choices=PET_TYPE_CHOICES,
		required=True,
		widget=forms.Select(
			attrs={
				'class': 'form-control',
			},
		),
	)
	name = forms.CharField(
		required=True,
		widget=forms.TextInput(
			attrs={
				'class': 'form-control',
			},
		),
	)
	age = forms.IntegerField(
		required=True,
		widget=forms.TextInput(
			attrs={
				'class': 'form-control',
				'type': 'number',
			},
		),
	)
	image_url = forms.URLField(
		required=True,
		widget=forms.TextInput(
			attrs={
				'class': 'form-control',
			},
		)
	)
	description = forms.CharField(
		required=True,
		widget=forms.Textarea(
			attrs={
				'class': 'form-control rounded-2',
			}
		)
	)

	class Meta:
		model = Pet
		fields = '__all__'
