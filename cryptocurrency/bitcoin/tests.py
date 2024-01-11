"""
Bitcoin app tests.
"""
import pytest

from .models import Bitcoin


@pytest.mark.django_db
class TestBitCoinModel:

    def test_ordering_meta_class_works_correctly(self):
        first_price = 'first'
        second_price = 'second'

        first_bitcoin = Bitcoin.objects.create(price=first_price)
        second_bitcoin = Bitcoin.objects.create(price=second_price)

        res = Bitcoin.objects.all()

        assert res[0].price == second_bitcoin.price
        assert res[1].price == first_bitcoin.price

        first_bitcoin.price = 'Edited'
        first_bitcoin.save()
        first_bitcoin.refresh_from_db()

        assert res[1].price == second_bitcoin.price
        assert res[0].price == first_bitcoin.price
