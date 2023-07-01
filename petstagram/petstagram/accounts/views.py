from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from petstagram.accounts.forms import AccountForm
from petstagram.accounts.models import Account

USER_MODEL = get_user_model()


@login_required
def account_details(request):
	user_id = request.user.id
	user = USER_MODEL.objects.get(pk=user_id)
	account = Account.objects.get(pk=user_id)
	if request.method == 'POST':
		form = AccountForm(request.POST, request.FILES, instance=account)
		if form.is_valid():
			form.save()
			return redirect('account details')
	else:
		form = AccountForm(instance=account)

	context = {
		'account_form': form,
		'account': account,
		'pets': user.pet_set.all(),
	}
	return render(request, 'accounts/user_account.html', context)
