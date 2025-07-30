from django.shortcuts import render
from django.http import HttpResponse
from .models import Photo

def gallery_view(request):
    photos = Photo.objects.all()
    # Debug: Print photos to console
    print("Photos in view:", list(photos.values('title', 'image')))
    
    # For debugging: Return raw data
    if request.GET.get('debug') == '1':
        return HttpResponse(f"<pre>Photos: {list(photos.values('title', 'image'))}</pre>")
        
    return render(request, 'gallery/gallery.html', {'photos': photos})
