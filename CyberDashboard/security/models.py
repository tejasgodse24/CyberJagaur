from django.db import models

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
