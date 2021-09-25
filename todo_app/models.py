from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save

# Create your models here.

class Profile(models.Model):
    first_name = models.CharField(max_length=255, blank=True,verbose_name='Adiniz')
    last_name = models.CharField(max_length=255, blank=True,verbose_name='Soyad')
    user = models.OneToOneField(User,on_delete = models.CASCADE,verbose_name='Hesab Adi')
    
    def __str__(self):
        return self.user.username

def create_user_profile(sender,instance,created,**kwargs):
        if created:
            Profile.objects.create(user=instance)
post_save.connect(create_user_profile,sender=settings.AUTH_USER_MODEL)

class ToDo(models.Model):
    description = models.CharField(max_length=255,verbose_name='Text',blank=False)
    finished = models.BooleanField(default=False)
    date_time = models.DateTimeField(auto_now_add=True)
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE,verbose_name='Hesab',related_name='istifadeci')
    
    def __str__(self):
        return self.description[:10]
    