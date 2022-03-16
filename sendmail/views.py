from django.conf import settings
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import render
from sendmail.models import Student


# from django.core.mail import send_mail

# Create your views here.


def home(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        b = Student(name=name, email=email)
        send_mail(
            subject='New car inquiry',
            message='https://google.com',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[email],
            fail_silently=False,
        )
        b.save()
    return render(request, 'home.html')
