from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    phone_number = models.CharField(
        max_length=15,
        blank=True
    )

class ShippingAddress(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    city = models.CharField(max_length=100)

    country = models.CharField(max_length=100)

    postal_code = models.CharField(max_length=20)

    address = models.TextField()

    def __str__(self):
        return f"{self.user.username} - {self.city}"