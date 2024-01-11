"""
Serializers for Bitcoin app.
"""
from rest_framework import serializers

from ..models import Bitcoin


class BitcoinSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bitcoin
        fields = ['price']
