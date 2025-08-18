from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt

from .models import Contact
from lionsfootball.models import Gallery
from gallery.models import Photo

# Create your views here.

def index(request):
    gallery_items = Gallery.objects.all()
    # Get the 4 most recent photos
    recent_photos = Photo.objects.all().order_by('-uploaded_at')[:4]
    return render(request, 'pages/index.html', {
        'gallery_items': gallery_items,
        'recent_photos': recent_photos
    })

from .forms import TrainingPhotoForm
from .models import TrainingPhoto

@require_http_methods(["GET", "POST"])
def training(request):
    if request.method == "POST":
        form = TrainingPhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Photo uploaded successfully!")
            return redirect('pages:training')
        else:
            messages.error(request, "There was an error uploading the photo. Please check the form.")
    else:
        form = TrainingPhotoForm()
    photos = TrainingPhoto.objects.filter(is_active=True).order_by('-created_at')
    return render(request, 'pages/training.html', {'photos': photos, 'form': form})

from .forms import TrainingPhotoForm, ContactForm

@require_http_methods(["GET", "POST"])
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({'success': True, 'message': 'Thank you for your message! We will get back to you soon.'})
            else:
                messages.success(request, 'Thank you for your message! We will get back to you soon.')
                return redirect('pages:contact')
        else:
            error_message = 'Please correct the errors below.'
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({'success': False, 'message': error_message, 'errors': form.errors}, status=400)
            messages.error(request, error_message)
    else:
        form = ContactForm()
    return render(request, 'pages/contact.html', {'form': form})