from django.db import models
from django.conf import settings

class Room(models.Model):
  name = models.CharField(max_length=50)
  description = models.CharField(max_length=200)
  price = models.DecimalField(max_digits=8, decimal_places=2)

  def __str__(self):
    return self.name

class Reservation(models.Model):
  STATUS_CHOICES = [
    ('pending', 'Pending'),
    ('approved', 'Approved' ),
    ('cancelled', 'Cancelled'),
  ]
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="reservations")
  reservation_time_start = models.DateTimeField()
  reservation_time_end = models.DateTimeField()
  status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

  def __str__(self):
    return f"{self.room} reservation: {self.reservation_time_start} - {self.reservation_time_end}"
