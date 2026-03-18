import os
from binance.client import Client
from dotenv import load_dotenv

load_dotenv()

class BinanceFuturesClient:
    def __init__(self):
        self.client = Client(
            os.getenv("BINANCE_API_KEY"),
            os.getenv("BINANCE_API_SECRET")
        )
        self.client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

    def place_order(self, **params):
        return self.client.futures_create_order(**params)
