from django import forms
from .models import TrainingPhoto

class TrainingPhotoForm(forms.ModelForm):
    class Meta:
        model = TrainingPhoto
        fields = ['title', 'image', 'is_active']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
