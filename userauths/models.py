from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from shortuuid.django_fields import ShortUUIDField
#create my custome user model 
class User(AbstractUser):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=100, blank=True, null= True)
    phone = models.CharField(max_length=100, blank=True, null= True)
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
    
    def __str__(self) -> str:
        return self.email
    
    def save(self, *args, **kwargs):
        email_username , _ = self.email.split("@")
        if self.full_name == "" or self.full_name == None:
            self.full_name = email_username
        if self.username == "" or self.username == None:
            self.username = email_username
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
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)
    
    #using shortuuid package
    pid = ShortUUIDField(unique=True, length=10, max_length=20, alphabet="abcdefghijklmnopqrstuv")
    
    def save(self, *args, **kwargs):
        if self.full_name == "" or self.full_name == None:
            self.full_name = self.user.full_name
        super(Profile, self).save(*args, **kwargs)
    
    def __str__(self):
        return str(self.full_name)
   
@receiver(post_save, sender=User)    
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    