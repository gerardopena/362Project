from django.db import models
from django.utils import timezone


# Create your models here.
class Flight(models.Model):
    origin = models.CharField(max_length=64)
    destination = models.CharField(max_length=64)
    date = models.IntegerField()
    
    def __str__(self):
        return f"{self.id} - {self.origin} to {self.destination} in {self.date} minutes."

