"""
Admin config for Bitcoin app.
"""
from django.contrib import admin

from .models import Bitcoin

admin.site.register(Bitcoin)
