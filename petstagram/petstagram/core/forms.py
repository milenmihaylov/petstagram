class BootstrapFormMixin:
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.__init_bootstrap_fields()

	def __init_bootstrap_fields(self):
		for (_, field) in self.fields.items():
			if 'class' not in field.widget.attrs:
				field.widget.attrs['class'] = ''
			else:
				field.widget.attrs['class'] += ' '
			field.widget.attrs['class'] += 'form-control'
			field.required = True
