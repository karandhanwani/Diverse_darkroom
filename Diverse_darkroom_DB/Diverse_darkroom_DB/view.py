from django.shortcuts import render,redirect
from DataBase_for_DiverseDarkroom.models import form
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.utils import timezone

def index(request):
    return render(request,'index.html')

def FormSubmit(request):
    if request.method=='POST':
        client = form()
        client.client_name = request.POST['name']
        client.client_email = request.POST['email']
        client.client_message = request.POST['message']
        client.message_draft_on = timezone.now().date()
        client.save()
        sendUserInfoToMail(client)
        return redirect('/')
    else:
        return render(request,'index.html',{'error':"A Problem occured, Form can't be submitted"})

def sendUserInfoToMail(client):
    mailTemplate = render_to_string('mail.html',{'client':client})
    email = EmailMessage(
        'New Order',
        mailTemplate,
        '',                 # Senders Email
        [''],               # Recievers Email
    )
    email.fail_silently = True
    email.send()
