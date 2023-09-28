from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    image = models.ImageField(default="default.jpg", upload_to = "profile_pics")
    
    def __str__(self) :
        return f'{self.user.username} Profile'
    
    def save(self,*arg, **kwargs):
        super(Profile,self).save(*arg, **kwargs)
        img = Image.open(self.image.path)
        print(f'Before Image Height :{img.height} and Width is : {img.width}')
        if img.height > 300 or img.width > 300 :
            print(f'Inside Logic : Image Height :{img.height} and Width is : {img.width}')
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path, "JPEG")
            
            
# Create your models here.
