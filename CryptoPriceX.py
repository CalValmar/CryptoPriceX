import requests     # https://docs.python-requests.org/en/master/   |   $ sudo pip install requests
import json         # https://docs.python.org/3/library/json.html
import time         # https://docs.python.org/3/library/time.html
import os           # https://docs.python.org/3/library/os.html

url ="https://api.binance.com/api/v3/ticker/price?symbol="

# ~~~~~~~~~~~ CryptoPriceX ~~~~~~~~~~~ # 
# request the API with the url and the currency pair
# return the price of the crypto

def request(url): 
    cours = requests.Session()
    response = cours.get(url)
    data = json.loads(response.text)
    return data["price"]

# list of crypto and their name
cryptos = {"  BTC": "Bitcoin", "  ETH": "Et hereum", "  LTC": "Litecoin", "  BCH": "Bitcoin Cash", "  ADA": "Cardano", "  XLM": "Stellar", "  EOS": "EOS",  "  DOGE": "Dogecoin",}

# list of fiduciary currencies and their name
fiduciaires = {"  USDT": "Dollar américain", "  EUR": "Euro", "  GBP": "Livre sterling", "  AUD": "Dollar australien", "  BRL": "Real brésilien"}

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')