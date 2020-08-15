from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from . forms import NewImageForm,EditProfileForm,CommentForm
from . models import Image,Profile,Comment,Following,Follower
from django.db import transaction
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import Http404,HttpResponseRedirect
from django.urls import reverse

@login_required(login_url="login")
def home(request):
    images = Image.all_images().order_by('-pub_date')
    return render(request, 'home.html', {'images':images})

def search_results(request):
    if 'search_profile' in request.GET and request.GET['search_profile']:
        name = request.GET.get("search_profile")
        results = Profile.search_profile(name)
        message = f'{name}'
        return render(request, 'search.html', {'results':results,'message':message})
    else:
        message = "User not found"
        return render(request, 'search.html', {'message': message})

def profile(request,id):
    user = get_object_or_404(User, id=id)
    images = Image.objects.filter(profile=user.id)
    return render (request,'profile/profile.html',{'images':images,'user':user})

# @transaction.atomic
# def other_profile(request):
#     try:
#         user = Profile.objects.get(user=username)
#     except:
#         raise Http404
#     if request.user.is_authenticated() and request.user == user:
#         images = Image.objects.filter(profile=user.id)
#     return render (request,'profile/other_profile.html', {'images':images,'user':user})

@login_required(login_url="login")
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

def post_by_id(request,id):
    image = Image.objects.get(id=id)
    comments = Comment.comments_on_image(id)
    form = CommentForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            comment = form.save(commit=False)
            comment.image = image
            comment.image.profile = request.user
            comment.save()
            HttpResponseRedirect('gram-single_post')
    return render(request,'single_image.html',{'image':image,'comments':comments,'form':form})
