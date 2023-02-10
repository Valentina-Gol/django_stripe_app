from django.db import models


class Item(models.Model):
    name = models.TextField(max_length=100)
    description = models.TextField(max_length=1000, blank=True)
    price = models.TextField(max_length=50)

    def __str__(self):
        return self.name
