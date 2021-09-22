from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='all-meetups'),
    path('<slug:meetup_slug>/success', views.confirm_registration, name='confirm-registration'),
    path('<slug:meetup_slug>', views.show_details, name='meetup-detail'),
]