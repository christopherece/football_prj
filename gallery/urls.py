from django.urls import path
from . import views

app_name = 'gallery'

urlpatterns = [
    path('', views.gallery_view, name='gallery'),
]
