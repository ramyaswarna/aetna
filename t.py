import requests

url = "https://2bb8-183-82-6-94.ngrok-free.app/search"
params = {"query": "EPIDIOLEX ORAL SOLUTION"}

response = requests.get(url, params=params)
print(response.json())  # Should return the response
