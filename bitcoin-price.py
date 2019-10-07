import requests

bitcoin_api_url = 'https://api.coinmarketcap.com/v1/ticker/bitcoin/'
response = requests.get(bitcoin_api_url)
response_json = response.json()
type(response_json)  # The API returns a list

print(response_json[0]['name'])
print(("Price: ") + (response_json[0]['price_usd']))
print(("Market cap: ") + (response_json[0]['market_cap_usd']))
