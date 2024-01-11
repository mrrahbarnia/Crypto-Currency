"""
Models for Bitcoin app.
"""
from django.db import models


class TimeStamp(models.Model):
    """Creating Timestamp model to inheriting in different models"""
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Bitcoin(TimeStamp):
    price = models.CharField(db_index=True, max_length=15)

    def __str__(self):
        return f'{self.price}'

    class Meta:
        """
        Ensure to retrieve the last one each
        time with celery task to process.
        """
        ordering = ('-updated_at',)
