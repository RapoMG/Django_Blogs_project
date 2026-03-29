from django.db import models
from django.contrib.auth.models import AbstractUser
from .validators import validate_username_not_email

# Create your models here.

class User(AbstractUser):
    email = models.EmailField(unique=True, blank=False, null=False)
    # Clone original field
    username = AbstractUser._meta.get_field("username").clone()
    # append aditional properties
    username.validators.append(validate_username_not_email)

    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    description = models.TextField(blank=True)
    is_email_visible = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username} profile'