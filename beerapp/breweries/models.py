from django.db import models

# Create your models here.
class Brewery(models.Model):
    """docstring for Brewery."""

    name = models.CharField(max_length=150)
    street = models.CharField(max_length=150)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    founded = models.DateField(null=True)

    def __str__(self):
        return self.name


class Beer(models.Model):
    """docstring for Beer."""

    name = models.CharField(max_length=75)
    abv = models.FloatField(null=True)
    brewery = models.ForeignKey(Brewery, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
