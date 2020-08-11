from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from . forms import NewImageForm,EditProfileForm
from . models import Image,Profile,Comment,Following,Follower
from django.db import transaction
from django.contrib import messages

@login_required(login_url="login")
def home(request):
    images = Image.all_images()
    return render(request, 'home.html', {'images':images})

@login_required
def profile(request):
    return render(request,'profile/profile.html')


@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        profile_form = EditProfileForm(request.POST, instance=request.user.profile)
        if profile_form.is_valid():            
            profile_form.save()
            messages.success(request,('Your profile was successfully updated!'))
            return redirect('gram-profile')
        else:
            messages.error(request,('Please correct the error below.'))
    else:
        profile_form = EditProfileForm(instance=request.user.profile)
    return render(request, 'profile/update_profile.html',{'profile_form': profile_form})

def new_image_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewImageForm(request.POST, request.FILES)
        if form.is_valid():
            image_post = form.save(commit=False)
            image_post.profile = current_user
            image_post.save()
        return redirect('gram-home')
    else:
        form = NewImageForm()
    return render(request,'new_post.html',{"form": form})