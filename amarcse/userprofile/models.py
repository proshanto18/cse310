from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30,null=True ,blank=True)
    last_name = models.CharField(max_length=30, null=True,blank=True)
    email = models.EmailField(null=True ,blank=True)
    phone_number = models.CharField(max_length=15,null=True ,blank=True)
    address = models.TextField(null=True ,blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    bio = models.TextField(null=True ,blank=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics/',null=True ,blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'