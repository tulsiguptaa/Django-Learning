from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField()
    age = models.IntegerField()
    email = models.EmailField()
    image = models.ImageField(upload_to='profiles', blank=True, null=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField()
    content = models.CharField()
    category = models.CharField(blank=True)

    def __str__(self):
        return self.title