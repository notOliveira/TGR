from django.db.models.signals import post_save, pre_delete
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile, Quiz

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()

@receiver(post_save, sender=User)
def create_quiz(sender, instance, created, **kwargs):
    if created:
        Quiz.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_quiz(sender, instance, **kwargs):
    instance.quiz.save()

@receiver(pre_delete, sender=User)
def delete_profile(sender, instance, **kwargs):
    if instance.profile.image and instance.profile.image.name != 'default_profile_picture_tgr4726hf8783.jpg':
        instance.profile.image.delete(save=False)