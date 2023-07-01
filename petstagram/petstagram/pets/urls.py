from django.urls import path
from petstagram.pets.views import pet_all, pet_detail, create_pet, edit_pet, delete_pet, comment_pet, like_pet

urlpatterns = [
	path('', pet_all, name='all pets'),
	path('details/<int:pk>/', pet_detail, name='pet detail'),
	path('like/<int:pk>/', like_pet, name='like'),
	# path('unlike/<int:pk>/', unlike_a_pet, name='unlike'),
	path('create/', create_pet, name='create pet'),
	path('edit/<int:pk>/', edit_pet, name='edit pet'),
	path('delete/<int:pk>', delete_pet, name='delete pet'),
	path('comment/<int:pk>', comment_pet, name='comment pet'),
]
