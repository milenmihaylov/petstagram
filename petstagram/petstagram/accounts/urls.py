from django.urls import path

from petstagram.accounts.views import account_details

urlpatterns = [
	path('', account_details, name='account details'),
]
