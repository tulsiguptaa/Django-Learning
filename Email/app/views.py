from django.core.mail import send_mail, EmailMessage, send_mass_mail
from django.http import HttpResponse
from django.template.loader import render_to_string


def send_email(request):
    send_mail(
        subject="Django Test",
        message="Hello! This email was sent from Django.",
        from_email=None,
        recipient_list=["nnainagupta836@gmail.com"],
        fail_silently=False,
    )

    return HttpResponse("Email sent successfully")

def send_email_msg(request):
    subject="Django Test"
    message=render_to_string('email/welcome.html', {'username':'Tulsi', 'course': 'django'})
    email = EmailMessage(subject, message, None, ['nnainagupta836@gmail.com'])
    email.content_subtype = "html"
    email.send()
    return HttpResponse("send")

def bulk_email(request):
    msg1 = ('welcome', 'hello', None, ['nnainagupta836@gmail.com'])
    msg2 = ('welcome', 'ironman', None, ['ironman9026@gmail.com'])

    send_mass_mail((msg1, msg2), fail_silently=False)
    return HttpResponse("Success")