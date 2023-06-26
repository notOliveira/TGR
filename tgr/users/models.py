from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    
    def __str__(self):
        return f'{self.user.username} - Profile'
    
    # Substituindo método save
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        
        width, height = img.size  # Get dimensions

        if width > 300 and height > 300:
            # keep ratio but shrink down
            img.thumbnail((width, height))

        # check which one is smaller
        if height < width:
            # make square by cutting off equal amounts left and right
            left = (width - height) / 2
            right = (width + height) / 2
            top = 0
            bottom = height
            img = img.crop((left, top, right, bottom))

        elif width < height:
            # make square by cutting off bottom
            left = 0
            right = width
            top = 0
            bottom = width
            img = img.crop((left, top, right, bottom))

        if width > 300 and height > 300:
            img.thumbnail((300, 300))

        img.save(self.image.path)

class Quiz(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    q1 = models.IntegerField(default=0)
    q2 = models.IntegerField(default=0)
    q3 = models.IntegerField(default=0)
    q4 = models.IntegerField(default=0)
    q5 = models.IntegerField(default=0)
    q6 = models.IntegerField(default=0)
    q7 = models.IntegerField(default=0)
    q8 = models.IntegerField(default=0)
    q9 = models.IntegerField(default=0)
    q10 = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.user.username} - Quiz"
