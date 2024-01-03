from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Accuracy_SQL(models.Model):
    model_name = models.CharField(max_length = 20)
    Accuracy_percentage = models.FloatField()
    def __str__(self):
        return self.model_name


class Accuracy_Phishing(models.Model) :
    model_name = models.CharField(max_length = 20)
    Accuracy_percentage = models.FloatField()
    def __str__(self):
        return self.model_name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    phone_number = models.CharField(max_length=10,null=True, blank=True)
