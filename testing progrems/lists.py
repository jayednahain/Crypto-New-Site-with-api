import json
import requests

api_request_price = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,XRP&tsyms=USD")
price_raw_data = json.loads(api_request_price.content)


value = "ETH"

listz=price_raw_data['DISPLAY'].keys()

listz.keys()