from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.core.mail import send_mail


@receiver(post_save, sender=User)
def send_welcome_email(sender, instance, created, **kwargs):

    if created:
        send_mail(
            "Welcome to our website!",
            f"Hello {instance.username}, welcome to our website.",
            "ttulsigupta836@gmail.com",
            [instance.email],
        )