from django.db import models

class userInformations(models.Model):
    id = models.CharField(max_length=12)
    password = models.CharField(max_length=12)

# Create your models here.
