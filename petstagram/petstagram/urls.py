from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from petstagram.common.views import testing_view

urlpatterns = [
    path('admin/', admin.site.urls),
	path('',  TemplateView.as_view(template_name='landing_page.html'), name='index'),
    path('testing/', testing_view, name='testing'),
    # path('home/', include('petstagram.common.urls')),
	path('pets/', include('petstagram.pets.urls')),
	path('auth/', include('petstagram.petstagram_auth.urls')),
	path('account/', include('petstagram.accounts.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
