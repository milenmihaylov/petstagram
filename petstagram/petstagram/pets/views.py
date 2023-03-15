from django.shortcuts import render, redirect

from petstagram.common.forms import CommentForm
from petstagram.common.models import Comment
from petstagram.pets.forms import PetCreateForm
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
	if request.method == 'GET':
		print(pet.comment_set.all()),
		context = {
			'pet': pet,
			'comments': pet.comment_set.all(),
			'comment_form': CommentForm()
		}
		return render(request, 'pet_detail.html', context)
	form = CommentForm(request.POST)
	if form.is_valid():
		Comment(
			pet=pet,
			comment=form.cleaned_data['comment'],
		).save()
		return redirect('pet detail', pk)
	context = {
		'pet': pet,
		'comments': ['First comment', 'Second comment'],
		'comment_form': form
	}
	return render(request, 'pet_detail.html', context)


def like_a_pet(request, pk):
	pet = Pet.objects.get(pk=pk)
	Like(
		pet=pet,
	).save()
	return redirect('pet detail', pk)


def create_pet(request):
	create_form = PetCreateForm(request.POST)
	if create_form.is_valid():
		create_form.save()
		return redirect('index')
	context = {
		'create_form': create_form,
	}
	return render(request, 'pet_create.html', context)


def edit_pet(request, pk):
	pet = Pet.objects.get(pk=pk)
	if request.method == 'GET':
		context = {
			'edit_form': PetCreateForm(initial=pet.__dict__)
		}
		return render(request, 'pet_edit.html', context)
	else:
		form = PetCreateForm(
			request.POST,
			instance=pet,
		)
		if form.is_valid():
			form.save()
			return redirect('all pets')
		context = {
			'edit_form': PetCreateForm(request.POST, instance=pet)
		}
		return render(request, 'pet_edit.html', context)


def delete_pet(request, pk):
	pet = Pet.objects.get(pk=pk)
	if request.method == 'GET':
		context = {
			'pet_name': pet.name
		}
		return render(request, 'pet_delete.html', context)
	else:
		pet.delete()
		return redirect('all pets')
