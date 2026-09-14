from django.shortcuts import render

def home(request):
    return render(request, 'blog/home.html', {'title': 'Home'})

def about(request):
    return render(request, 'blog/about.html', {'content': 'About Page'})

def contact(request):
    return render(request, 'blog/contact.html')