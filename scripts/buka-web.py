import requests

url = "https://github.com/n-research"
response = requests.get(url)

print(f"Status: {response.status_code}")
