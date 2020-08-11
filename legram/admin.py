from django.contrib import admin
from . models import Profile,Image,Comment,Follower,Following

admin.site.register(Profile)
admin.site.register(Image)
admin.site.register(Comment)
admin.site.register(Follower)
admin.site.register(Following)


