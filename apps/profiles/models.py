from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    objects = models.Manager()

    class Meta:
        verbose_name = "profile"
        verbose_name_plural = "profiles"

    def __str__(self):
        return self.user.username
