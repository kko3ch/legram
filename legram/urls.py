from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name = 'gram-home'),
    url(r'profile/', views.profile, name = 'gram-profile'),
    url(r'profile/update_profile/', views.update_profile, name = 'gram-profile-update'),
    url(r'new_post/', views.new_image_post, name = 'gram-post'),
]