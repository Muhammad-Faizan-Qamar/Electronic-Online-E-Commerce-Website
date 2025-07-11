from django.shortcuts import render
from .forms import ContactInformation

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    ci = ContactInformation()
    return render(request, 'contact.html', {"form":ci})

def product(request):
    return render(request, 'product.html')

def cart(request):
    return render(request, 'cart.html')

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')

