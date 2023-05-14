
from django.db import models

class Meet(models.Model):
    name = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    description = models.TextField(max_length=1000000)
    image = models.ImageField(upload_to='images/')
    days = models.CharField(max_length=400)

    def __str__(self):
        return self.name




