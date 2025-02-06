import requests

url = "http://127.0.0.1:5000/upload_pdf"
file_path = r"C:\Users\ramya\Downloads\2025_Aetna_Health_Exchange_Plan_CA_PPO.pdf"

files = {"file": open(file_path, "rb")}
response = requests.post(url, files=files)

print(response.json())
