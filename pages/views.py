from django.shortcuts import render
from lionsfootball.models import Gallery

# Create your views here.

def index(request):
    gallery_items = Gallery.objects.all()
    return render(request, 'pages/index.html', {'gallery_items': gallery_items})

def training(request):
    return render(request, 'pages/training.html')