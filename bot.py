from binance.client import Client
from decouple import config

API_KEY = config('API_KEY')
API_SECRET = config('SECRET_KEY')

client = Client()

orderbook = client.get_order_book(symbol="ETHUSDT")

print(orderbook)
