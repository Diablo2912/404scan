import requests
from bs4 import BeautifulSoup

def csrf(url, timeout=10):
    try:
        response = requests.get(url, timeout=timeout)
        content = response.text
        cookies = response.cookies.get_dict()

        soup = BeautifulSoup(content, "html.parser")

        findings = {
            "hidden_inputs": [],
            "meta_tags": [],
            "cookies": [],
        }

        # Look for hidden input fields with common CSRF names
        for hidden in soup.find_all("input", {"type": "hidden"}):
            name = hidden.get("name", "").lower()
            if "csrf" in name or "token" in name:
                findings["hidden_inputs"].append({name: hidden.get("value")})

        # Look for meta tags with CSRF tokens
        for meta in soup.find_all("meta"):
            name = meta.get("name", "").lower() if meta.get("name") else ""
            if "csrf" in name:
                findings["meta_tags"].append({name: meta.get("content")})

        # Look for cookies that might be CSRF-related
        for cookie_name, cookie_value in cookies.items():
            if "csrf" in cookie_name.lower() or "xsrf" in cookie_name.lower():
                findings["cookies"].append({cookie_name: cookie_value})

        return findings

    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    target_url = input("Enter the URL: ")
    csrf_token = csrf(target_url)
    print(csrf_token)