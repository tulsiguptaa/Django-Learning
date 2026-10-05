from django.db import models

class User(models.Model):
    username = models.CharField()
    email = models.EmailField()

    def __str__(self):
        return self.username
