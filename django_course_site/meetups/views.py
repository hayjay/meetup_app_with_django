from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegistrationForm
from .models import Meetup, Participant

# Create your views here.
def welcome(request):
    meetups = Meetup.objects.all()
    # print(meetups[2]['slug'])
    return render(request, 'meetups/index.html', {
        'meetups': meetups,
        'show_meetups': True
    })

def show_details(request, meetup_slug):
    # print(meetup_slug)
    try:
        selected_meetup = Meetup.objects.get(slug=meetup_slug)
        if request.method == 'GET':
            registration_form = RegistrationForm()
            return render(request, 'meetups/meetup-details.html', {
                'meetup': selected_meetup,
                'location': 'Cool',
                'meetup_found': True,
                'form': registration_form,
            })
        else:
            # //validate user input
            registration_form = RegistrationForm(request.POST) #GET THE FORM DATA HERE
            if registration_form.is_valid(): #if email field and other fields are validated successfully
                #participant = registration_form.save() #calling save returns an insert of the saved model (participant in this case)
                user_email = registration_form.cleaned_data['email']
                participant, was_created = Participant.objects.get_or_create(email=user_email) #works like first or create. get_or_create returns a tupple
                selected_meetup.participants.add(participant) #add newly registered participant into this current meetup as a related table
                #redirect the user after successfully registering
                return redirect('confirm-registration', meetup_slug=meetup_slug)
        return render(request, 'meetups/meetup-details.html', {
            'meetup': selected_meetup,
            'location': 'Cool',
            'meetup_found': True,
            'form': registration_form,
        })
    except Exception as exc:
        print(exc)
        return render(request, 'meetups/meetup-details.html', {
            'meetup_found': False
        })

def confirm_registration(request, meetup_slug):
    meetup = Meetup.objects.get(slug=meetup_slug) #where slug = meetup_slug - SQL
    return render(request, 'meetups/registration-success.html', {
        'organizer_email': meetup.organizer_email
    })
