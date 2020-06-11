from django.db import models
from django.conf import settings

# Create your models here.

class PlaidToken(models.Model):
    access_token = models.CharField(max_length=64, default='')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('access_token', 'user')
