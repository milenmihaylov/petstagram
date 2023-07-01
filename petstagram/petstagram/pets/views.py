from django.contrib.auth.decorators import login_required
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
	return render(request, 'pets/pet_list.html', context)


@login_required()
def pet_detail(request, pk):
	pet = Pet.objects.get(pk=pk)
	pet.likes_count = pet.like_set.count()
	is_liked_by_user = pet.like_set.filter(user_id=request.user.id).exists()
	is_owner = pet.user == request.user
	if request.method == 'GET':
		context = {
			'pet': pet,
			'comments': pet.comment_set.all(),
			'comment_form': CommentForm(),
			'is_liked': is_liked_by_user,
			'is_owner': is_owner,
		}
		return render(request, 'pets/pet_detail.html', context)


@login_required()
def comment_pet(request, pk):
	pet = Pet.objects.get(pk=pk)
	form = CommentForm(request.POST)
	if form.is_valid():
		Comment(
			pet=pet,
			comment=form.cleaned_data['comment'],
			user=request.user
		).save()
	return redirect('pet detail', pet.id)


@login_required()
def like_pet(request, pk):
	pet = Pet.objects.get(pk=pk)
	like_object_by_user = pet.like_set.filter(user_id=request.user.id).first()
	if like_object_by_user:
		like_object_by_user.delete()
	else:
		Like(
			pet=pet,
			user=request.user,
		).save()
	return redirect('pet detail', pet.id)


@login_required()
def create_pet(request):
	if request.method == 'GET':
		context = {
			'create_form': PetCreateForm()
		}
		return render(request, 'pets/pet_create.html', context)
	create_form = PetCreateForm(request.POST, request.FILES)
	if create_form.is_valid():
		pet = create_form.save(commit=False)
		pet.user = request.user
		pet.save()
		return redirect('all pets')
	context = {
		'create_form': create_form,
	}
	return render(request, 'pets/pet_create.html', context)


@login_required()
def edit_pet(request, pk):
	pet = Pet.objects.get(pk=pk)
	if request.method == 'GET':
		context = {
			'edit_form': PetCreateForm(instance=pet)
		}
		return render(request, 'pets/pet_edit.html', context)
	else:
		form = PetCreateForm(
			request.POST,
			request.FILES,
			instance=pet,
		)
		if form.is_valid():
			form.save()
			return redirect('all pets')
		context = {
			'edit_form': PetCreateForm(request.POST, request.FILES, instance=pet)
		}
		return render(request, 'pets/pet_edit.html', context)


@login_required()
def delete_pet(request, pk):
	pet = Pet.objects.get(pk=pk)
	if request.method == 'GET':
		context = {
			'pet_name': pet.name
		}
		return render(request, 'pets/pet_delete.html', context)
	else:
		pet.delete()
		return redirect('all pets')
