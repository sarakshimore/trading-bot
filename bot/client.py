from dotenv import load_dotenv
from binance.client import Client
import os

load_dotenv()

API_KEY = os.getenv("BINANCE_API_KEY")
API_SECRET = os.getenv("BINANCE_API_SECRET")

def get_client():
    client = Client(
        api_key=API_KEY,
        api_secret=API_SECRET,
        demo=True
    )

    return client