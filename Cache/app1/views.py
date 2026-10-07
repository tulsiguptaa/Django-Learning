from django.shortcuts import render
from django.core.cache import caches
from django.http import HttpResponse

def file_cache(request):
    file_cache = caches["file_cache"]

    file_cache.set("course", "Django", 60)

    course = file_cache.get("course")
    return HttpResponse(f"course: {course}")
