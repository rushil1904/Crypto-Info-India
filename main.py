import requests
import json

base_api = 'https://api.wazirx.com/'
market_status = requests.get(base_api + '/api/v2/market-status').json()
market_ticker = requests.get(base_api + '/api/v2/tickers').json()
market_depth = requests.get(base_api + '/api/v2/depth').json()
market_trade_history = requests.get(base_api + '/api/v2/trades').json()

def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

btc = print("BTC: "), jprint(market_ticker['btcinr'])
eth = print("ETH: "), jprint(market_ticker['ethinr'])
doge = print("Doge: "), jprint(market_ticker['dogeinr'])
matic = print("Matic: "), jprint(market_ticker['maticinr'])
shibu = print("Shibu: "), jprint(market_ticker['shibinr'])