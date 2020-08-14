from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.db.models.signals import post_save
from django.dispatch import receiver

class Follower(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name

class Following(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name

class Profile(models.Model):
    '''
    Profile model that links with User to update it
    '''
    user = models.OneToOneField(User, on_delete=models.CASCADE,null = True)
    first_name = models.CharField(max_length=30, blank=True)
    second_name = models.CharField(max_length=30, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/',null=True)
    birth_date = models.DateField(null=True, blank=True)
    followers = models.ForeignKey(Follower,on_delete=models.CASCADE,null=True)
    following = models.ForeignKey(Following,on_delete=models.CASCADE,null=True)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
    
    def save_profile(self):
        self.user

    def delete_profile(self):
        self.delete()

    @classmethod
    def search_profile(cls, name):
        return cls.objects.filter(user__username__icontains=name).all()

    def __str__(self):
        return f'{self.user.username}'

class Comment(models.Model):
    '''
    class that defines a category object
    '''
    name = models.CharField(max_length =30)

    def save_comment(self):
        self.save()

    def delete_comment(self):
        self.delete()

    @classmethod
    def all_comments(cls):
        return cls.objects.all()

    def __str__(self):
        return self.name

class Image(models.Model):
    '''
    class that defines an instance of Image
    '''
    image = models.ImageField(upload_to='images/',null=True)
    name = models.CharField(max_length =30)
    caption = models.CharField(max_length=100)
    profile = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    likes = models.ManyToManyField(User, related_name='images')
    comments = models.ForeignKey(Comment,on_delete=models.CASCADE,null=True)
    pub_date = models.DateTimeField(auto_now_add=True)

    class meta:
        ordering =['name']
    
    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod 
    def all_images(cls):
        return cls.objects.all()

    @classmethod
    def images_by_profile(cls,profile):
        profile_name = Profile.objects.get(user = profile)
        images = cls.objects.filter(location=profile_name.id)
        return images
    
    def __str__(self):
        return self.name