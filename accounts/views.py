from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,get_user_model,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
from . forms import UserRegisterForm,UserLoginForm
from django.contrib.auth.models import Group

def register_view(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            new_user = User.objects.create_user(username = username,email = email)
            new_user.save()
            messages.success(request, f'Account created for {username}')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/register.html',{'form': form})
