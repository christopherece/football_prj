from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from .forms import UserRegistrationForm, ProfileUpdateForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('accounts:user_profile')
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})

from django.shortcuts import get_object_or_404
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required

@login_required
def profile_edit(request, user_id):
    user = get_object_or_404(User, id=user_id)
    # Only allow editing own profile or if staff
    if not (request.user == user or request.user.is_staff):
        return HttpResponseForbidden("You do not have permission to edit this profile.")
    profile = user.profile
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            # Update User info
            user.first_name = request.POST.get('first_name', user.first_name)
            user.last_name = request.POST.get('last_name', user.last_name)
            user.email = request.POST.get('email', user.email)
            user.save()
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('user_detail', user_id=user.id)
    else:
        form = ProfileUpdateForm(instance=profile)
    return render(request, 'accounts/profile_edit.html', {'form': form, 'profile_user': user})

@login_required
def user_profile(request):
    if request.user.is_staff:
        return redirect('/adminpanel/users/')
    profile = request.user.profile
    return render(request, 'accounts/user_profile.html', {'user': request.user, 'profile': profile})
