from django.urls import path
from petstagram.pets.views import pet_all, pet_detail, like_a_pet

urlpatterns = [
	path('', pet_all, name='list pets'),
	path('details/<int:pk>/', pet_detail, name='pet details'),
	path('like/<int:pk>/', like_a_pet, name='like'),
]
