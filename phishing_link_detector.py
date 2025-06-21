
# phishing_link_detector.py
import re
from urllib.parse import urlparse

suspicious_keywords = ['login', 'verify', 'update', 'secure', 'account', 'bank', 'paypal', 'signin']

def is_ip_in_url(url):
    ip_pattern = r'http[s]?://(?:[0-9]{1,3}\.){3}[0-9]{1,3}'
    return re.match(ip_pattern, url) is not None

def has_suspicious_keywords(url):
    for keyword in suspicious_keywords:
        if keyword in url.lower():
            return True
    return False

def is_long_url(url):
    return len(url) > 75

def check_url(url):
    print(f"\n[🔎] Scanning: {url}\n")

    if is_ip_in_url(url):
        print("⚠️  Contains IP address instead of domain")

    if has_suspicious_keywords(url):
        print("⚠️  Suspicious keyword found in URL")

    if is_long_url(url):
        print("⚠️  URL is too long")

    parsed = urlparse(url)
    if not parsed.scheme or not parsed.netloc:
        print("❌ Invalid URL format.")
    else:
        print("✅ Basic URL format seems OK")

    print("\n✔️  Scan complete.\n")

if __name__ == "__main__":
    user_url = input("Enter the URL to scan: ")
    check_url(user_url)
