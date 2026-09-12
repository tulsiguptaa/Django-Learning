from django.shortcuts import render

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def home(request):
    context = {
        "name": "Tulsi Gupta",
        "age" : 21, 
        "skills" : ['Python', 'ML', 'Gen AI'],
        "user": User('naina', 21)
    }
    return render(request, 'home.html', context=context)
