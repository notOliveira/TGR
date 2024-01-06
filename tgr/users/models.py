from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from .constants import Q1_CHOICES, Q2_CHOICES, Q3_CHOICES, Q4_CHOICES, Q5_CHOICES, Q6_CHOICES, Q7_CHOICES

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default_profile_picture_tgr4726hf8783.jpg', upload_to='profile_pics')
    
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
    q1 = models.CharField(max_length=25, choices=Q1_CHOICES)
    q2 = models.CharField(max_length=25, choices=Q2_CHOICES)
    q3 = models.CharField(max_length=25, choices=Q3_CHOICES)
    q4 = models.CharField(max_length=25, choices=Q4_CHOICES)
    q5 = models.CharField(max_length=25, choices=Q5_CHOICES)
    q6 = models.CharField(max_length=25, choices=Q6_CHOICES)
    q7 = models.CharField(max_length=25, choices=Q7_CHOICES)
    
    def __str__(self):
        return f"{self.user.username} - Quiz"