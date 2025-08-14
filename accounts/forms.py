from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['date_of_birth'] = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
        self.fields['phone_number'] = forms.CharField(required=False, max_length=20)
        self.fields['address'] = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows': 3}))
        self.fields['emergency_contact'] = forms.CharField(required=False, max_length=100)
        self.fields['emergency_phone'] = forms.CharField(required=False, max_length=20)

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.save()
        profile = Profile.objects.create(user=user)
        profile.date_of_birth = self.cleaned_data['date_of_birth']
        profile.phone_number = self.cleaned_data['phone_number']
        profile.address = self.cleaned_data['address']
        profile.emergency_contact = self.cleaned_data['emergency_contact']
        profile.emergency_phone = self.cleaned_data['emergency_phone']
        profile.save()
        return user
