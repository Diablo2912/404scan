import socket
import requests
import logging

def get_ip_domain(domain: str):
    try:
        ip_address = socket.gethostbyname(domain)
        print(f"IP Address: {ip_address}")
        return ip_address
    except socket.gaierror:
        print("Could not resolve IP address for the domain")
        return None
    
def get_ip_country(ip_address):
    try:
        r = requests.get(f"https://ipwho.is/{ip_address}", timeout=5)
        data = r.json()
        if data.get("success"):
            country_code = data.get("country_code", "Unknown")
            country_name = data.get("country", "Unknown")
            print(f" GeoIP: {country_name} ({country_code})")
            return country_code
        return "Unknown"
    except Exception as e:
        print("GeoIP Error:", e)
        return "Unknown"
    
def reverse_dns(ip_address):
    try:
        hostname, _, _ = socket.gethostbyaddr(ip_address)
        print(f'PTR: {hostname}')
        return hostname
    except socket.herror:
        return "No PTR record found"
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    target_domain = input("Enter the domain to perform DNS enumeration: ").strip()
    ip_address = get_ip_domain(target_domain)
    country = get_ip_country(ip_address)
    dns = reverse_dns(ip_address)