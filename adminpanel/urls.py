from django.urls import path
from . import views
from accounts import views as accounts_views

urlpatterns = [
    path('login/', views.admin_login, name='admin_login'),
    path('users/', views.user_list, name='user_list'),
    path('users/<int:user_id>/', views.user_detail, name='user_detail'),
    path('users/<int:user_id>/edit/', accounts_views.profile_edit, name='profile_edit'),
]
