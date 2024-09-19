from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.exceptions import ValidationError


class Customer(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    date_of_birth = models.DateField()
    phone_number = PhoneNumberField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
