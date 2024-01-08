"""
Models for Bitcoin app.
"""
from django.db import models


class Bitcoin(models.Model):
    price = models.CharField(max_length=10)

    def __str__(self):
        return f'Currently price is {self.price}'
