from django.db import models

# Create your models here.


class School(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    pincode = models.CharField(max_length=10)

    def __str__(self):
        return self.name
