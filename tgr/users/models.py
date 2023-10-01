from django.db import models
from django.contrib.auth.models import User
from PIL import Image

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
    OPT_Q1 = (
        # Playstation
        ('playstation_1', 'Playstation 1'),
        ('playstation_2', 'Playstation 2'),
        ('playstation_3', 'Playstation 3'),
        ('playstation_4', 'Playstation 4'),
        ('playstation_5', 'Playstation 5'),
        ('playstation_psp', 'Playstation Portable (PSP)'),
        ('playsation_vita', 'Playstation Vita'),
        # Xbox
        ('xbox','Xbox'),
        ('xbox_360','Xbox 360'),
        ('xbox_one','Xbox One'),
        ('xbox_x','Xbox Series S/X'),
        ('xbox_kinect','Kinect'),
        # Nintendo
    )
    
    OPT_Q2 = (
        ('opção1', 'Opção 1'),
        ('opção2', 'Opção 2'),
        ('opção3', 'Opção 3'),
    )
    
    OPT_Q3 = (
        ('opção1', 'Opção 1'),
        ('opção2', 'Opção 2'),
        ('opção3', 'Opção 3'),
    )
    
    OPT_Q4 = (
        ('opção1', 'Opção 1'),
        ('opção2', 'Opção 2'),
        ('opção3', 'Opção 3'),
    )
    
    OPT_Q5 = (
        ('opção1', 'Opção 1'),
        ('opção2', 'Opção 2'),
        ('opção3', 'Opção 3'),
    )

    OPT_Q6 = (
        ('opção1', 'Opção 1'),
        ('opção2', 'Opção 2'),
        ('opção3', 'Opção 3'),
    )
    
    OPT_Q7 = (
        ('opção1', 'Opção 1'),
        ('opção2', 'Opção 2'),
        ('opção3', 'Opção 3'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    q1 = models.CharField(max_length=50, choices=OPT_Q1, default='opção1')
    q2 = models.CharField(max_length=50, choices=OPT_Q2, default='opção1')
    q3 = models.CharField(max_length=50, choices=OPT_Q3, default='opção1')
    q4 = models.CharField(max_length=50, choices=OPT_Q4, default='opção1')
    q5 = models.CharField(max_length=50, choices=OPT_Q5, default='opção1')
    q6 = models.CharField(max_length=50, choices=OPT_Q6, default='opção1')
    q7 = models.CharField(max_length=50, choices=OPT_Q7, default='opção1')
    
    def __str__(self):
        return f"{self.user.username} - Quiz"