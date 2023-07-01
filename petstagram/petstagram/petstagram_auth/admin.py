from django.contrib import admin
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.admin import UserAdmin


USER_MODEL = get_user_model()


@admin.register(USER_MODEL)
class PetstagramUserAdmin(UserAdmin):
	list_display = ('username', 'is_staff')
	list_filter = ('is_staff', 'is_superuser', 'groups')
	fieldsets = (
		(None, {'fields': ('username', 'password')}),
		(_('Permissions'), {
			'fields': ('is_staff', 'is_superuser', 'groups', 'user_permissions'),
		}),
		(_('Important dates'), {'fields': ('last_login', 'date_joined')}),
	)
	readonly_fields = ('date_joined', 'last_login')
