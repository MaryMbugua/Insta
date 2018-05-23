from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver
from tinymce.models import HTMLField

# Create your models here.

class ProfileManager(models.Manager):
    use_for_related_fields = True

    def all(self):
        qs = self.get_queryset().all()
        try:
            if self.instance:
                qs = qs.exclude(user=self.instance)
        except:
            pass
        return qs


class Profile(models.Model):
    profile_pic = models.ImageField(upload_to='avatar/', blank=True)
    bio = HTMLField()
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    first_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=30, null=True)
    following = models.ManyToManyField(User, blank=True, related_name='followed_by')

    objects = ProfileManager()

    def get_following(self):
        users = self.following.all()
        return users.exclude(username=self.user.username)

    def __str__(self):
        return self.first_name

    @classmethod
    def get_all_profiles(cls):
        profile = Profile.objects.all()
        return profile

    @classmethod
    def get_searched_profile(cls, search_term):
        profiles = cls.objects.filter(first_name__icontains=search_term)
        return profiles

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    @receiver(post_save, sender=User)
    def update_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
        instance.profile.save()


class Image(models.Model):
    pic = models.ImageField(upload_to='images/', blank=True)
    caption = models.CharField(max_length=60, null=True)
    likes = models.ManyToManyField(User, related_name='likes', blank=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True)

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def __str__(self):
        return self.caption

    @classmethod
    def get_images(cls):
        images = cls.objects.all()
        return images

    def total_likes(self):
        return self.likes.count()


class Comment(models.Model):
    comment = models.CharField(max_length=50)
    image = models.ForeignKey(Image, null=True)
    user = models.ForeignKey(User, null=True)

    def __str__(self):
            return self.comment