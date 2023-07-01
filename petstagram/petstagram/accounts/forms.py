from django import forms

from petstagram.accounts.models import Account
from petstagram.core.forms import BootstrapFormMixin


class AccountForm(BootstrapFormMixin, forms.ModelForm):
	class Meta:
		model = Account
		exclude = ('user',)
		widgets = {
			'picture': forms.FileInput()
		}
