from django.db import models

class Gallery(models.Model):
    app_label = 'lionsfootball'
    CATEGORY_CHOICES = [
        ('training', 'Training'),
        ('matches', 'Matches'),
        ('events', 'Events'),
        ('awards', 'Awards'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='gallery/')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
