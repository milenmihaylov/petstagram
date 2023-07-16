from os.path import join

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView

from petstagram import settings
from petstagram.common.forms import CommentForm, CommentModelFormForCBV
from petstagram.core.clean_up import clean_up_files
from petstagram.core.views import PostOnlyView, BootstrapFromViewMixin
from petstagram.pets.forms import EditPetForm
from petstagram.pets.models import Pet, Like
from petstagram.petstagram_auth.mixins import LoginRequiredMixin


class PetListView(LoginRequiredMixin, ListView):
	model = Pet
	template_name = 'pets/pet_list.html'
	context_object_name = 'pets'


class PetDetailView(LoginRequiredMixin, DetailView):
	model = Pet
	template_name = 'pets/pet_detail.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		self.object.likes_count = self.object.like_set.count()
		context['comments'] = self.object.comment_set.all()
		context['comment_form'] = CommentForm
		context['is_liked'] = self.object.like_set.filter(user_id=self.request.user.id).exists()
		context['is_owner'] = self.object.user == self.request.user
		return context


class CommentPetView(LoginRequiredMixin, FormView):
	form_class = CommentModelFormForCBV

	def form_valid(self, form):
		comment = form.save(commit=False)
		comment.user = self.request.user
		comment.pet = Pet.objects.get(pk=self.kwargs['pk'])
		comment.save()
		return redirect('pet detail', self.kwargs['pk'])


# @login_required()
# def like_pet(request, pk):
# 	pet = Pet.objects.get(pk=pk)
# 	like_object_by_user = pet.like_set.filter(user_id=request.user.id).first()
# 	if like_object_by_user:
# 		like_object_by_user.delete()
# 	else:
# 		Like(
# 			pet=pet,
# 			user=request.user,
# 		).save()
# 	return redirect('pet detail', pet.id)


class LikePetView(LoginRequiredMixin, View):

	def get(self, request, pk):
		pet = Pet.objects.get(pk=pk)
		like_object = pet.like_set.filter(user_id=request.user.id).first()
		if like_object:
			like_object.delete()
		else:
			Like(
				pet=pet,
				user=request.user
			).save()
		return redirect('pet detail', pk)


class PetCreateView(LoginRequiredMixin, BootstrapFromViewMixin, CreateView):
	model = Pet
	template_name = 'pets/pet_create.html'
	fields = ('name', 'description', 'image', 'age', 'type')

	def form_valid(self, form):
		pet = form.save(commit=False)
		pet.user = self.request.user
		pet.save()
		return super().form_valid(form)

	def get_success_url(self):
		return reverse_lazy('pet detail', kwargs={'pk': self.object.id})


class PetUpdateView(LoginRequiredMixin, UpdateView):
	model = Pet
	template_name = 'pets/pet_edit.html'
	form_class = EditPetForm

	def form_valid(self, form):
		old_image = self.get_object().image
		if old_image:
			clean_up_files(join(settings.MEDIA_ROOT, str(old_image)))
		return super().form_valid(form)

	def get_success_url(self):
		return reverse_lazy('pet detail', kwargs={'pk': self.object.id})


class PetDeleteView(LoginRequiredMixin, DeleteView):
	model = Pet
	template_name = 'pets/pet_delete.html'
	success_url = reverse_lazy('all pets')
