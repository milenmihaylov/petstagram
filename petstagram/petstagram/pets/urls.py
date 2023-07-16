from django.urls import path
from petstagram.pets import views

urlpatterns = [
	# path('', pet_all, name='all pets'),
	path('', views.PetListView.as_view(), name='all pets'),
	# path('details/<int:pk>/', views.pet_detail, name='pet detail'),
	path('details/<int:pk>/', views.PetDetailView.as_view(), name='pet detail'),
	# path('like/<int:pk>/', views.like_pet, name='like'),
	path('like/<int:pk>/', views.LikePetView.as_view(), name='like'),
	# path('create/', views.create_pet, name='create pet'),
	path('create/', views.PetCreateView.as_view(), name='create pet'),
	# path('edit/<int:pk>/', views.edit_pet, name='edit pet'),
	path('edit/<int:pk>/', views.PetUpdateView.as_view(), name='edit pet'),
	# path('delete/<int:pk>', views.delete_pet, name='delete pet'),
	path('delete/<int:pk>', views.PetDeleteView.as_view(), name='delete pet'),
	# path('comment/<int:pk>', views.comment_pet, name='comment pet'),
	path('comment/<int:pk>', views.CommentPetView.as_view(), name='comment pet'),
]
