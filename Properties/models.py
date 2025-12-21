from django.db import models

class Card(models.Model):
    title = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='card_images/', blank=True, null=True)

    def __str__(self):
        return self.title
    
class Contact(models.Model):
    name = models.CharField(max_length=100 )
    phone = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name
    
class Client(models.Model):
    name = models.CharField(max_length=100)
    message = models.TextField()
    client_pic = models.ImageField(upload_to='client/', blank=True, null=True)
    
    
    def __str__(self):
        return self.name
    
    
    # Create your models here.
    
class Arch(models.Model):
    TYPE_CHOICES = [
        ('INTERIOR', 'Interior'),
        ('EXTERIOR', 'Exterior'),
    ]
    type = models.CharField(max_length=100, choices=TYPE_CHOICES)  # Correct field
    image = models.ImageField(upload_to='arch_images/')
    title = models.CharField(max_length=200)
    description = models.TextField()
    video = models.FileField(upload_to='arch_videos/', null=True, blank=True)

    def __str__(self):
        return str (self.type)+ " " +str(self.title)
