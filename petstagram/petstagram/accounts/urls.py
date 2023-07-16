from django.urls import path

from petstagram.accounts.views import AccountDetailsView

urlpatterns = [
	# path('', account_details, name='account details'),
	path('', AccountDetailsView.as_view(), name='account details'),
]


