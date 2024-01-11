"""
Consumers config.
"""
import json
import requests
import asyncio

from channels.generic.websocket import AsyncJsonWebsocketConsumer
from asgiref.sync import sync_to_async

# 45,487.695

class Watch:

    def __init__(self):
        self.task: asyncio.Task = None
        self.futures: list[asyncio.Future] = []

    def start(self):
        if self.task:
            return
        self.task = asyncio.create_task(self.get_price_loop())

    async def get_price_loop(self):
        while True:
            await self.get_price()
            await asyncio.sleep(5)
    
    async def get_price(self):
        url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
        response = await sync_to_async(requests.get)(url)
        res = json.loads(response.text)
        currently_price = res['bpi']['USD']['rate']
        for future in self.futures:
            if future.cancelled():
                continue
            future.set_result(currently_price)
        self.futures.clear()
    
    def add_future(self, future):
        self.futures.append(future)
    

watch = Watch()


class BitcoinChartConsumer(AsyncJsonWebsocketConsumer):

    async def get_price(self):
        watch.start()
        while True:
            future = asyncio.Future()
            watch.add_future(future)
            # pass future to somewhere where can be fulfilled
            price = await future
            await self.send_json({'price': price})

    async def connect(self):
        await self.accept()
        self.task = asyncio.create_task(self.get_price())

    async def disconnect(self, code):
        self.task.cancel()
