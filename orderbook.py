from binance.client import Client
from pandas import DataFrame as df
from datetime import datetime
import keys
import json

client = Client(api_key=keys.Pkey, api_secret=keys.Pkey)
order = client.get_order_book(symbol='BNBBTC')
print(order)




