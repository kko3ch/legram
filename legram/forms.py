from . models import Image,Profile,Comment
from django import forms

class NewImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['profile','likes','comments','pub_date']

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['profile','followers','following']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['image','name','pub_date']
        widgets = {
            'body': forms.Textarea(attrs={'class':'form-control','required': 'false'})
        }