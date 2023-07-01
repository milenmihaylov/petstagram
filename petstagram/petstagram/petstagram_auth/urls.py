from django.urls import path

from petstagram.petstagram_auth.views import signup_user, login_user, logout_user

urlpatterns = [
	path('signup/', signup_user, name='signup'),
	path('login/', login_user, name='login'),
	path('logout/', logout_user, name='logout'),
]
