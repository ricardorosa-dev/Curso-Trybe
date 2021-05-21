import requests

response = requests.get("http://httpbin.org/status/404")
response.raise_for_status()
