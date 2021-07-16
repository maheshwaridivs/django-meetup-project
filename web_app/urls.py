from django.urls import path
# from .views import *
from . import views

#path is function which takes numbe of arguments
urlpatterns = [
	path('meetups/', views.meetups,name="all-meetups"),  # we are calling index function from views.py file
	path('meetups/<slug>/success',views.confirm_registration,name="confirm-registration"),
	path('meetups/<slug>',views.meetupDetails,name="meetup-detail"),
	
]

# path('meetups/<slug:meetup_slug>/success',views.confirm_registration,name="confirm-registration"),
# path('meetups/<slug:meetup_slug>',views.meetupDetails,name="meetup-detail"),