from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home/',views.home , name = "home"), 
    path('about/',views.about,name ="about"),
    path('auth/',views.auth,name ="auth"),
    path("contact/",views.contact,name ="contact"),
    path('interior/',views.interior , name = "interior"),
    path('exterior/',views.exterior , name = "exterior"),    
    path('properties/', views.properties , name="properties"),

    path('Termandconditions/',views.Termandconditions , name = "Termandconditions"),
    path('Privacy/',views.Privacy , name = "Privacy"),
    path('Documentation/',views.Documentation , name = "Documentation")

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)