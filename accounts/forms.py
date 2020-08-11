from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='valid email address.')
    class meta:
        model = User
        fields = ('username','email','password1','password2',)

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username,password=password)
            if not user:
                raise forms.ValidationError('user does not exist')
            if not user.check_password(password):
                raise forms.ValidationError('incorrect password')
            if not user.is_active:
                raise forms.ValidationError('User is not active')
        
        return super(UserLoginForm, self).clean(*args, *kwargs)