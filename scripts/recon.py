import requests

subdomains = ["admin", "api", "dev", "test"]
target = "target.com"

for sub in subdomains:
    url = f"https://{sub}.{target}"
    try:
        r = requests.get(url, timeout=5)
        print(f"{url} → {r.status_code}")
    except:
        pass
        