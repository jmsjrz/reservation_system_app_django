# models.py

from django.db import models
from django.contrib.auth.models import User

class TimeSlot(models.Model):
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.date} {self.start_time}-{self.end_time}"

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time_slot = models.ForeignKey(TimeSlot, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Mettre à jour la disponibilité du créneau lors de la création ou la mise à jour d'une réservation
        self.time_slot.available = False
        self.time_slot.save()
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        # Mettre à jour la disponibilité du créneau lors de la suppression d'une réservation
        self.time_slot.available = True
        self.time_slot.save()
        super().delete(*args, **kwargs)

    def __str__(self):
        return f"{self.user} - {self.time_slot}"
