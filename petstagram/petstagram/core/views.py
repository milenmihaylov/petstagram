from django.views import View


class PostOnlyView(View):
	def post(self, request, *args, **kwargs):
		form = self.form_class(request.POST)
		if form.is_valid():
			return self.form_valid(form)
		else:
			return self.form_invalid(form)

	def form_valid(self, form):
		pass

	def form_invalid(self, form):
		pass


class BootstrapFromViewMixin:

	def get_form(self, **kwargs):
		form = super().get_form(**kwargs)
		self.__apply_bootstrap_classes(form)
		return form

	@staticmethod
	def __apply_bootstrap_classes(form):
		for (_, field) in form.fields.items():
			if 'class' not in field.widget.attrs:
				field.widget.attrs['class'] = ''
			else:
				field.widget.attrs['class'] += ' '
			field.widget.attrs['class'] += 'form-control'

