"""
Utility functions to use in Airflow DAGs.
Author: Andrew Jarombek
Date: 11/9/2021
"""

from typing import List, Dict, Union

import requests
from requests import Response


def get_bitcoin_price(**context):
    response: Response = requests.get('https://api2.binance.com/api/v3/ticker/24hr')
    eth_info: List[Dict[str, Union[str, int]]] = [item for item in response.json() if item.get('symbol') == 'BTCUSDT']

    print(f"Checking price on {context.get('ds')}")

    if len(eth_info) == 0:
        print(f"Bitcoin Price Not Found")
    else:
        price = "${:,.2f}".format(float(eth_info[0].get('lastPrice')))
        print(f"Bitcoin Price: {price}")
