from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    SEX_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    POSITION_CHOICES = [
        ('GK', 'Goalkeeper'),
        ('DF', 'Defender'),
        ('MF', 'Midfielder'),
        ('FW', 'Forward'),
        ('OT', 'Other'),
    ]
    FOOT_CHOICES = [
        ('R', 'Right'),
        ('L', 'Left'),
        ('B', 'Both'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='profile_photos/', blank=True, null=True)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    nationality = models.CharField(max_length=50, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)
    guardian_name = models.CharField(max_length=100, blank=True)
    guardian_phone = models.CharField(max_length=20, blank=True)
    emergency_contact = models.CharField(max_length=100, blank=True)
    emergency_phone = models.CharField(max_length=20, blank=True)
    playing_position = models.CharField(max_length=2, choices=POSITION_CHOICES, blank=True)
    preferred_foot = models.CharField(max_length=1, choices=FOOT_CHOICES, blank=True)
    medical_conditions = models.TextField(blank=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.user.username
