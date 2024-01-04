import requests

payload = {'key': '9B4C80763C9402E38824BDA5439E8BA8', 'ip': '8.8.8.8', 'format': 'json'}
api_result = requests.get('https://api.ip2location.io/', params=payload)
json_data = api_result.json()
print(json_data.get('latitude'))