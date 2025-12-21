from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def home(request):
    cards = Card.objects.all()
    exterior = Arch.objects.filter(type="EXTERIOR")
    interior = Arch.objects.filter(type="INTERIOR")
    clients = Client.objects.all()
    
    return render(request, 'home.html', {"exterior": exterior,"agents": interior,"clients": clients,"cards": cards})

def about(request):
    return render(request,"about.html")

def contact(request):
    print(request.method)
    if request.method =='POST':
        print("inside")
        name  = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        Contact.objects.create(
            name  = name,
            phone = phone,
            email=email,
            message = message,
        )
        
    print("ouside")
    return render(request,"contact.html")
