from typing import List, Dict, Union

import requests
from requests import Response


def get_bitcoin_price() -> float:
    response: Response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    price = response.json().get('bpi').get('USD').get('rate_float')
    return price


def get_ethereum_price():
    response: Response = requests.get('https://api2.binance.com/api/v3/ticker/24hr')
    eth_info: List[Dict[str, Union[str, int]]] = [item for item in response.json() if item.get('symbol') == 'ETHUSDT']
    price = 0.0 if len(eth_info) == 0 else float(eth_info[0].get('lastPrice'))
    return price
