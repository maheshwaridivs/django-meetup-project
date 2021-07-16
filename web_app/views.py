from django.shortcuts import render, redirect
from django.http import HttpResponse
from web_app.models import *
from .forms import RegistrationForm

# Create your views here.


def meetups(request):
    meetups = Meetup.objects.all()
    return render(request, 'index.html', {'meetups': meetups})


# it takes argument from url and which is slug id and name should be same
def meetupDetails(request, slug):
    print("-------meetup_slug-----------",slug)
    try:
        selected_meetup = Meetup.objects.get(slug=slug)
        if request.method == 'GET':
            registation_form = RegistrationForm()
        else:
            registation_form = RegistrationForm(request.POST)
            if registation_form.is_valid():
                # participant = registation_form.save()
                user_email = registation_form.cleaned_data['email']
                participant, _ = Participant.objects.get_or_create(
                    email=user_email)
                selected_meetup.participants.add(participant)
                return redirect('confirm-registration',slug=slug)
        return render(request, 'meetup-details.html',
                      {'meetup': selected_meetup, 'meetup_found': True,
                       'form': registation_form})
    except Exception as exc:
        print(exc)
        return render(request, 'meetup-details.html', {'meetup_found': False})


def confirm_registration(request, slug):
    meetup = Meetup.objects.get(slug=slug)
    return render(request, 'registration.html',{'organizer_email':meetup.organizer_email
        })
