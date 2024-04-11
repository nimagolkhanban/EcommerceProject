from django.db import models
from django.contrib.auth.models import AbstractUser
from shortuuid.django_fields import ShortUUIDField
#create my custome user model 
class User(AbstractUser):
    username = models.CharField(max_lrngth=100)
    email = models.Emailfields(unique=True)
    full_name = models.CharField(max_length=100, blank=True, null= True)
    phone = models.CharField(max_length=100, blank=True, null= True)
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
    
    def __str__(self) -> str:
        return self.email
    
    def save(self, *args, **kwargs):
        email_username , _ = self.email.split("@")
        if self.full_name == "" or self.full_name == None:
            self.full_name = self.email
        if self.username == "" or self.username == None:
            self.username = self.email
        super(User, self).save(*args, **kwargs)
        
            


    
    
    
    
    