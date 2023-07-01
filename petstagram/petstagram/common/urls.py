from petstagram.common.views import landing_page, testing_view
from django.urls import path

urlpatterns = [
    path('', landing_page, name='index'),
    path('testing/', testing_view, name='testing'),
]

