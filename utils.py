import requests
import json
from config import keys

class ConvertionExaption(Exception):
    pass

class CriptoConverter:
    @staticmethod
    def convert(quote: str, base: str, amount: str):
        if quote == base:
            raise ConvertionExaption(f'не возможно перевести валюту в себя же {base}..')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionExaption(f'не удалось конвертировать валюту {quote}')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionExaption(f'не удалось конвертировать валюту {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionExaption(f'не удалось обработать колличество{amount}')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = json.loads(r.content)[keys[base]]

        return total_base
