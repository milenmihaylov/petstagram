from django.shortcuts import render, redirect

from petstagram.pets.models import Pet, Like


def pet_all(request):
	all_pets = Pet.objects.all()
	context = {
		'pets': all_pets
	}
	return render(request, 'pet_list.html', context)


def pet_detail(request, pk):
	pet = Pet.objects.get(pk=pk)
	pet.likes_count = pet.like_set.count()
	context = {
		'pet': pet,
	}
	return render(request, 'pet_detail.html', context)


def like_a_pet(request, pk):
	pet = Pet.objects.get(pk=pk)
	Like(
		pet=pet,
	).save()
	return redirect('pet details', pk)
