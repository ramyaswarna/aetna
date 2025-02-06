import requests

url = "http://127.0.0.1:5000/search"
params = {"query": "EPIDIOLEX OR cannabidiol OR Epidiolex Oral Solution"}

response = requests.get(url, params=params)

# ✅ Print raw response content before JSON decoding
print("Raw Response:", response)

