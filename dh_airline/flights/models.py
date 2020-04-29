from django.db import models
from django.utils import timezone
from django.urls import reverse


# Create your models here.
class Flight(models.Model):
    origin = models.CharField(max_length=64)
    destination = models.CharField(max_length=64)
    duration = models.IntegerField()
    seats = 24

    def __str__(self):
        return f"{self.origin} to {self.destination} in {self.duration} minutes."

    def get_absolute_url(self):
        return reverse(
            'flights:detailpage',
            kwargs={
                "dest": self.destination,
                "orig": self.origin,
                "pk": self.pk

            }
        )

class Confirmation(models.Model):
    confirmation = models.CharField(max_length=8)
    flight = models.ForeignKey(Flight, related_name='flight', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
