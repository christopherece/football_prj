from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class UserRegistrationForm(UserCreationForm):
    date_of_birth = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    phone_number = forms.CharField(required=False, max_length=20)
    address = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows': 3}))
    emergency_contact = forms.CharField(required=False, max_length=100)
    emergency_phone = forms.CharField(required=False, max_length=20)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',
                  'date_of_birth', 'phone_number', 'address',
                  'emergency_contact', 'emergency_phone')
