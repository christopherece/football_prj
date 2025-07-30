from django.db import models
from django.utils import timezone
from django.utils.text import slugify

# Create your models here.

def training_photo_upload_path(instance, filename):
    # This will create a path like: training_photos/2025/07/28/filename.jpg
    date_path = timezone.now().strftime('%Y/%m/%d')
    return f'training_photos/{date_path}/{filename}'

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - {self.subject}"

# class TrainingPhoto(models.Model):
#     title = models.CharField(max_length=200, help_text="A descriptive title for the photo")
#     image = models.ImageField(upload_to=training_photo_upload_path, help_text="Upload a training photo")
#     is_active = models.BooleanField(default=True, help_text="Uncheck to hide this photo from the training page")
#     created_at = models.DateTimeField(default=timezone.now)

#     class Meta:
#         ordering = ['-created_at']
#         verbose_name = 'Training Photo'
#         verbose_name_plural = 'Training Photos'

#     def __str__(self):
#         return self.title
