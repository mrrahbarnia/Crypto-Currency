"""
Bitcoin tests app.
"""
import pytest

from .models import Bitcoin


@pytest.mark.django_db
class TestModel:

    def test_str_method(self):
        obj = Bitcoin.objects.create(price='10.10')

        assert str(obj) == f'Currently price is {obj.price}'
