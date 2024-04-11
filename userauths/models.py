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
        
            

class Profile(models.Model):
    
    class GenderChoice(models.TextChoices):
        male = "male",
        femail = "femail",
        other = "other"
        
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    #the reaseon we use image field is becaus image have various amont of format
    image = models.ImageField(upload_to="image", default="default/default-image.jpg", null=True, blank=True)
    
    full_name = models.CharField(max_length=100, blank=True, null= True)
    abount = models.TextField(null=True, blank=True)
    gender = models.CharField(choices=GenderChoice.choices, default=GenderChoice.male, max_length=6)
    state = models.CharField(max_lrngth=50)
    city = models.CharField(max_lrngth=50)
    address = models.CharField(max_lrngth=500)
    date = models.DateTimeField(auto_now_add=True)
    
    #using shortuuid package
    pid = ShortUUIDField(unique=True, length=10, max_length=20, alphabets="abcdefghijklmnopqrstuv")
    
    def save(self, *args, **kwargs):
        if self.full_name == "" or self.full_name == None:
            self.full_name = self.user.full_name
        super(Profile, self).save(*args, **kwargs)
    
    
    
    
    
    