from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField()
    course = models.CharField()

    def __str__(self):
        return self.username