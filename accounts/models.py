from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Profile(models.Model):
    
    class ServiceCategory(models.TextChoices):
        PLUMBER = 'Plumber', 'Plumber'
        ELECTRICIAN = 'Electrician', 'Electrician'
        CARPENTER = 'Carpenter', 'Carpenter'
        MECHANIC = 'Mechanic', 'Mechanic'
        CLEANING = 'Cleaning', 'Cleaning'
        IT = 'IT Services', 'IT Services'
        Tile = 'Tile', 'Tile'
        Mistri = 'Mason/Mistri', 'Mason/Mistri'
        OTHER = 'Other', 'Other'
         
        
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    service_id = models.CharField(
        max_length=20,
        unique=True,
        blank=True
    )
    
    profile_pic = models.ImageField(upload_to='profiles/', blank=True, null=True)
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    service_category = models.CharField(
        max_length=50,
        choices=ServiceCategory.choices,
        default=ServiceCategory.OTHER
    )
    work = models.CharField(max_length=100)
    work_description = models.TextField(blank=True)
    experience = models.CharField(max_length=50)
    address = models.TextField()
    location = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.service_id:
            today = timezone.now().strftime('%d%m%y')  # 301225

            # Count profiles created today
            count_today = Profile.objects.filter(
                created_at__date=timezone.now().date()
            ).count() + 1

            self.service_id = f"ar@{today}{count_today:03d}"

        super().save(*args, **kwargs)

    def __str__(self):
        return self.user.username
