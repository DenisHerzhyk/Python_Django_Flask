from django.db import models


class Clients(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    number = models.CharField(max_length=100)
    address = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name} {self.surname}"
