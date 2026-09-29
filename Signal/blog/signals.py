from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from .models import Blog

@receiver(pre_save, sender=Blog)
def before_blog_save(sender, instance, **kwargs):
    print(f"Abou to save blog[pre_save]: {instance.title}")


@receiver(post_save, sender=Blog)
def after_blog_save(sender, instance, created, **kwargs):
    if created: 
        print(f"New blog created[post_save] : {instance.title}")
    else:
        print(f"Blog updated[Post-save]: {instance.title}")