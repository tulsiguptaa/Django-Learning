from django.db import models
from django.urls import reverse
# Create your models here.
class Post(models.Model):
    title = models.CharField()
    content = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", args=[self(self.id)])
    