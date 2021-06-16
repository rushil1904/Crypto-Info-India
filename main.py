import requests
import json

base_api = 'https://api.wazirx.com/'
#API Endpoints
market_status = requests.get(base_api + '/api/v2/market-status').json()
market_ticker = requests.get(base_api + '/api/v2/tickers').json()
market_depth = requests.get(base_api + '/api/v2/depth?market={}'.format('btcinr')).json()
market_trade_history = requests.get(base_api + '/api/v2/trades?market={}'.format('btcinr')).json()

def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

print("Welcome to the world of crypto!!")
print("For help enter: '\help'")
response = input('What would you like to know: ')
if 'exchange' in response:
  btc = print("BTC: "), jprint(market_ticker['btcinr'])
  eth = print("ETH: "), jprint(market_ticker['ethinr'])
  doge = print("Doge: "), jprint(market_ticker['dogeinr'])
  matic = print("Matic: "), jprint(market_ticker['maticinr'])
  shibu = print("Shibu: "), jprint(market_ticker['shibinr'])

if 'status' in response:
  jprint(market_status['markets']), jprint(market_status['assets'])

