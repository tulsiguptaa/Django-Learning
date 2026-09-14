from django.contrib import admin
from contact.models import User
# Register your models here.

@admin.register(User)
class Admin(admin.ModelAdmin):
    list_filter = ('name', 'email')