import json
import requests

from datetime import timedelta
from celery import shared_task

from cryptocurrency.celery_config import app
from .models import Bitcoin

app.conf.beat_schedule = {
    'crawl_bitcoin_price': {
        'task': 'bitcoin.tasks.crawl_bitcoin_price',
        'schedule': timedelta(seconds=15)
    }
}


@shared_task
def crawl_bitcoin_price():
    url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
    response = requests.get(url)
    res = json.loads(response.text)
    currently_price = res['bpi']['USD']['rate']

    bit_obj = Bitcoin.objects.get(id=1)
    bit_obj.price = currently_price
    bit_obj.save()