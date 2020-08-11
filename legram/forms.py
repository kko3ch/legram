from . models import Image,Profile
from django import forms

class NewImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['profile','likes','comments','pub_date']

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['profile','followers','following']