from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.contrib import messages


def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_staff:
            login(request, user)
            return redirect('user_list')
        else:
            messages.error(request, 'Invalid credentials or not an admin user.')
    return render(request, 'adminpanel/login.html')


def is_admin(user):
    return user.is_staff


@login_required(login_url='admin_login')
@user_passes_test(is_admin, login_url='admin_login')
def user_list(request):
    users = User.objects.all().order_by('-date_joined')
    return render(request, 'adminpanel/user_list.html', {'users': users})

@login_required(login_url='admin_login')
@user_passes_test(is_admin, login_url='admin_login')
def user_detail(request, user_id):
    user_obj = get_object_or_404(User, id=user_id)
    return render(request, 'adminpanel/user_detail.html', {'user_obj': user_obj})
