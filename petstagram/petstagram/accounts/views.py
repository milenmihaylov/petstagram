from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import FormView, DetailView, UpdateView

from petstagram.accounts.forms import AccountForm
from petstagram.accounts.models import Account
from petstagram.petstagram_auth.mixins import LoginRequiredMixin

USER_MODEL = get_user_model()


# @login_required
# def account_details(request):
# 	user_id = request.user.id
# 	user = USER_MODEL.objects.get(pk=user_id)
# 	account = Account.objects.get(pk=user_id)
# 	if request.method == 'POST':
# 		form = AccountForm(request.POST, request.FILES, instance=account)
# 		if form.is_valid():
# 			form.save()
# 			return redirect('account details')
# 	else:
# 		form = AccountForm(instance=account)
#
# 	context = {
# 		'account_form': form,
# 		'account': account,
# 		'pets': user.pet_set.all(),
# 	}
# 	return render(request, 'accounts/user_account.html', context)


class AccountDetailsView(LoginRequiredMixin, UpdateView):
	model = Account
	template_name = 'accounts/user_account.html'
	form_class = AccountForm
	success_url = reverse_lazy('account details')

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['account'] = self.get_object()
		context['pets'] = self.request.user.pet_set.all()
		return context

	def get_object(self, queryset=None):
		user_id = self.request.user.id
		account = Account.objects.get(pk=user_id)
		return account


