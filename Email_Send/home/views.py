from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail


# def home(request):
#     subject = 'Sending Love'
#     message = "I saw that you were perfect, and so I loved you. Then I saw that you were not perfect and I loved you even more."
#     email_from = settings.EMAIL_HOST_USER
#     recipient_list = ['chinmayrai75@gmail.com']
#     send_mail( subject, message, email_from, recipient_list )


#     return render(request,'home.html')

def index(request):
  return render(request, 'index.html')


def mail(request):
    subject = request.POST['subject']
    message = request.POST['message']
    email_from = settings.EMAIL_HOST_USER
    mail=request.POST['email']
    recipient_list = [mail,]
    send_mail( subject, message, email_from, recipient_list )
    return render(request,'home.html')
# Create your views here.
