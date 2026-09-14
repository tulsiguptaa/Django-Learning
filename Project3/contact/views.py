from django.shortcuts import render

# Create your views here.
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        return render(request, 'submit.html', {
            'name': name,
            'email': email
        })
    return render(request, 'contact/contact.html')