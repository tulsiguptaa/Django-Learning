from django.core.mail import send_mail
from django.http import HttpResponse


def send_email(request):
    send_mail(
        subject="Django Test",
        message="Hello! This email was sent from Django.",
        from_email=None,
        recipient_list=["nnainagupta836@gmail.com"],
        fail_silently=False,
    )

    return HttpResponse("Email sent successfully")