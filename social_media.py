import re
import requests

def social_media(url, timeout=10):
    try:
        response = requests.get(url, timeout=timeout)  # sends a GET request to the website
        content = response.text  # raw HTML of the page

        # Regex pattern to match social media links
        pattern = r'(https?://(?:www\.)?(?:facebook|twitter|instagram)\.com/[^"\'>\s]+)'
        links = re.findall(pattern, content, re.IGNORECASE)

        return links
    
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return []
    
def emails(url, timeout=10):
    try:
        response = requests.get(url, timeout=timeout) 
        content = response.text  # raw HTML of the page

        email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[A-Za-z]{2,}"
        emails = re.findall(email_pattern, content, re.IGNORECASE)

        return emails
    
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return []


if __name__ == "__main__":
    target_url = input("Enter the URL to fetch links from: ")
    social_media_links = social_media(target_url)
    email_address = emails(target_url)

    if social_media_links:
        print("\nFound social media links:")
        for link in social_media_links:
            print(link)
    else:
        print("No social media links found.")

    if email_address:
        print("\nFound emails:")
        for email in email_address:
            print(email)
    else:
        print("No emails found.")