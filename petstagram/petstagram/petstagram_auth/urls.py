from django.urls import path

from petstagram.petstagram_auth import views

urlpatterns = [
	# path('signup/', views.signup_user, name='signup'),
	path('signup/', views.SignUpUserView.as_view(), name='signup'),
	# path('login/', login_user, name='login'),
	path('login/', views.LoginUserView.as_view(), name='login'),
	# path('logout/', views.logout_user, name='logout'),
	path('logout/', views.LogoutUserView.as_view(), name='logout'),
]
