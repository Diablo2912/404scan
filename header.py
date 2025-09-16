import requests
from urllib.parse import urlparse
import logging

def normalize_url(u):
    if not urlparse(u).scheme:
        return "https://" + u
    return u

def fetch_headers(url):
    url = normalize_url(url)
    try:
        r = requests.head(url, timeout=10, headers={"User-Agent":"SafeHeaderCheck/1.0"}, allow_redirects=True, verify=True)
        headers = dict(r.headers)
        return {"headers": headers, "status_code": r.status_code, "error": None}
    except requests.RequestException as e:
        return {"headers": {}, "status_code": None, "error": str(e)}

if __name__ == "__main__":
    target_url = input("Enter the URL to fetch headers from: ")
    headers_data = fetch_headers(target_url)
    print(headers_data)