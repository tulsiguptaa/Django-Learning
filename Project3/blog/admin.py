from django.contrib import admin
from blog.models import Students

# Register your models here.

# admin.site.register(Students)

@admin.register(Students)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'age')
    search_fields = ('name', 'age')
    list_filter = ('name', 'age')