from petstagram.common.views import testing_view, LandingPageView
from django.urls import path

urlpatterns = [
    path('', LandingPageView.as_view(), name='index'),
    path('testing/', testing_view, name='testing'),
]

