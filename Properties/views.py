from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import *
from django.core.mail import EmailMultiAlternatives
from django.views.decorators.cache import cache_page
from django.core.paginator import Paginator
from django.core.mail import send_mail
from django.conf import settings
# from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
@cache_page(60 * 30)
def home(request):
    cards = Card.objects.all()
    exterior = Arch.objects.filter(type="EXTERIOR")
    interior = Arch.objects.filter(type="INTERIOR")
    clients = Client.objects.all()
    
    return render(request, 'home.html', {"exterior": exterior,"agents": interior,"clients": clients,"cards": cards})

@cache_page(60 * 30)
def about(request):
    return render(request,"about.html")

# def contact(request):
#     print(request.method)
#     if request.method =='POST':
#         print("inside")
#         name  = request.POST.get('name')
#         phone = request.POST.get('phone')
#         email = request.POST.get('email')
#         message = request.POST.get('message')
        
#         Contact.objects.create(
#             name  = name,
#             phone = phone,
#             email=email,
#             message = message,
#         )
        
#     print("ouside")
#     return render(request,"contact.html")
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        subject = "New Service Inquiry – Contact Form Submission"
        from_email = settings.DEFAULT_FROM_EMAIL
        to_email = ['gargy5703@gmail.com', 'Ar.jawed.m@gmail.com']
        html_content = f"""
            <!DOCTYPE html>
            <html>
            <head>
            <meta charset="UTF-8">
            </head>
            <body style="font-family: Arial, sans-serif; font-size: 18px; color: #333;">
                <p style="font-size: 22px;">You have received a new service inquiry through the website contact form.</p>

                <p><strong>Name:</strong> {name}</p>
                <p><strong>Email:</strong> {email}</p>
                <p><strong>Phone:</strong> {phone}</p>

                <p><strong>Message:</strong></p>
                <h2 style="
                    font-size: 18px;
                    line-height: 1.6;
                    background-color: #f4f4f4;
                    padding: 15px;
                    border-radius: 5px;
                ">
                    {message}
                </h2>

                <p style="margin-top: 20px;">
                    Please contact the client at your earliest convenience.
                </p>
                <p>Regards,</p>
                <p>Website Contact System</p>
            </body>
            </html>
            """

# body = f"""
# Dear Team,

# You have received a new service inquiry through the website contact form.

# Client Details:
# -------------------------
# Name   : {name}
# Email  : {email}
# Phone  : {phone}

# Message:
# -------------------------
# {message}

# Please review the inquiry and contact the client at your earliest convenience.

# Regards,
# Website Contact System
# """

        # send_mail(
        #     subject,
        #     body,
        #     settings.DEFAULT_FROM_EMAIL,   # sender
        #     ['gargy5703@gmail.com', 'Ar.jawed.m@gmail.com'],       # receiver
        #     fail_silently=False,
        # )
        email_msg = EmailMultiAlternatives(
            subject,
            "",  # no plain text
            from_email,
            to_email
        )

        # ✅ Attach HTML
        email_msg.attach_alternative(html_content, "text/html")
        email_msg.send()

        messages.success(request, "Your message has been sent successfully!")
        return redirect('contact')

    return render(request, 'contact.html')


@cache_page(60 * 10)
def interior(request):
    interior = Arch.objects.filter(type="INTERIOR")
    for helo in interior:
      print(helo.type)
    paginator = Paginator(interior, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    for interior in page_obj:
        print(interior.image)
    return render(request,"interior.html", {'page_obj': page_obj})


@cache_page(60 * 10)
def exterior(request):
    exterior = Arch.objects.filter(type="EXTERIOR")
    paginator = Paginator(exterior, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    for archs in page_obj:
        print(archs.image)
    return render(request,"exterior.html", {'page_obj': page_obj})
 
 
@cache_page(60 * 10)
def properties(request):
    cards = Card.objects.all()
    
    paginator = Paginator(cards, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number) 
    
    for card in page_obj:
        print(card.image)
    return render(request,"prop.html", {'page_obj': page_obj})


def auth(request):
    return render(request,"auth.html")

def Termandconditions(request):
    return render(request,"Conditions.html")
def Privacy(request):
    return render(request,"Privacy.html")
def Documentation(request):
    return render(request,"Cookies.html")
