from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path('', views.index, name='index'),
    path('training/', views.training, name='training'),
    path('contact/', views.contact, name='contact'),
]