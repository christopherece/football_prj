from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['photo', 'sex', 'date_of_birth', 'nationality', 'phone_number', 'address', 'guardian_name', 'guardian_phone', 'emergency_contact', 'emergency_phone', 'playing_position', 'preferred_foot', 'medical_conditions', 'notes']
        widgets = {
            'sex': forms.Select(attrs={'class': 'form-control'}),
            'date_of_birth': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'nationality': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'rows': 2, 'class': 'form-control'}),
            'guardian_name': forms.TextInput(attrs={'class': 'form-control'}),
            'guardian_phone': forms.TextInput(attrs={'class': 'form-control'}),
            'emergency_contact': forms.TextInput(attrs={'class': 'form-control'}),
            'emergency_phone': forms.TextInput(attrs={'class': 'form-control'}),
            'playing_position': forms.Select(attrs={'class': 'form-control'}),
            'preferred_foot': forms.Select(attrs={'class': 'form-control'}),
            'medical_conditions': forms.Textarea(attrs={'rows': 2, 'class': 'form-control'}),
            'notes': forms.Textarea(attrs={'rows': 2, 'class': 'form-control'}),
        }

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['first_name'] = forms.CharField(required=True, max_length=30)
        self.fields['last_name'] = forms.CharField(required=True, max_length=150)
        self.fields['email'] = forms.EmailField(required=True)
        self.fields['date_of_birth'] = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
        self.fields['sex'] = forms.ChoiceField(required=False, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')])
        self.fields['photo'] = forms.ImageField(required=False)
        self.fields['nationality'] = forms.CharField(required=False, max_length=50)
        self.fields['phone_number'] = forms.CharField(required=False, max_length=20)
        self.fields['address'] = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows': 3}))
        self.fields['guardian_name'] = forms.CharField(required=False, max_length=100)
        self.fields['guardian_phone'] = forms.CharField(required=False, max_length=20)
        self.fields['emergency_contact'] = forms.CharField(required=False, max_length=100)
        self.fields['emergency_phone'] = forms.CharField(required=False, max_length=20)
        self.fields['playing_position'] = forms.ChoiceField(required=False, choices=[('GK', 'Goalkeeper'), ('DF', 'Defender'), ('MF', 'Midfielder'), ('FW', 'Forward'), ('OT', 'Other')])
        self.fields['preferred_foot'] = forms.ChoiceField(required=False, choices=[('R', 'Right'), ('L', 'Left'), ('B', 'Both')])
        self.fields['medical_conditions'] = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows': 2}))
        self.fields['notes'] = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows': 2}))

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.save()
        profile = Profile.objects.create(user=user)
        profile.date_of_birth = self.cleaned_data['date_of_birth']
        profile.sex = self.cleaned_data['sex']
        profile.photo = self.cleaned_data['photo']
        profile.nationality = self.cleaned_data['nationality']
        profile.phone_number = self.cleaned_data['phone_number']
        profile.address = self.cleaned_data['address']
        profile.emergency_contact = self.cleaned_data['emergency_contact']
        profile.emergency_phone = self.cleaned_data['emergency_phone']
        profile.save()
        return user
