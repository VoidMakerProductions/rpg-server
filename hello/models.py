from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class IPStore(models.Model):
    ip = models.CharField(max_length=256)
