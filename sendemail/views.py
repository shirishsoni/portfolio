from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ContactForm
from django.contrib import messages
from .models import Emails

def contactView(request):
    if request.method == 'GET':
        form = ContactForm()
        #return render(request, "sendemail/email.html", {'form': form})
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            email = Emails()
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            email.subject = subject
            email.email_from = from_email
            email.message = message
            email.save()
            try:
                send_mail(subject, message+from_email, from_email,['shirishsoni12@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('home')
    return render(request, "sendemail/email.html", {'form': form})

def successView(request):
    return HttpResponse('Success! Thank you for your message.')

# Create your views here.
