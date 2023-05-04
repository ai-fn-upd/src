from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class Movie(models.Model):
    title = models.CharField()
    description = models.TextField(null=True)
    release_date = models.DateTimeField()
    preview = models.ImageField(default="", null=True)
    likes = models.ManyToManyField(User, null=True, related_name="liked_movies")

    def __str__(self):
        return self.title


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
