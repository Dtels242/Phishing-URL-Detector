import re
from urllib.parse import urlparse

# Suspicious phishing patterns
suspicious_keywords = ["secure", "free", "login", "verify", "account", "bank", "update", "password"]
ip_url_pattern = r"http[s]?://(?:[0-9]{1,3}\.){3}[0-9]{1,3}"

def is_phishing_url(url):
    parsed_url = urlparse(url)
    domain = parsed_url.netloc

    if re.match(ip_url_pattern, url):
        return True, "IP-based URL detected (Potential phishing attempt)."

    for keyword in suspicious_keywords:
        if keyword in domain.lower() or keyword in url.lower():
            return True, f"Suspicious keyword '{keyword}' found in URL."

    if len(url) > 75:
        return True, "URL length is unusually long."

    return False, "URL seems safe."

# Test URLs
test_urls = [
    "http://secure-login-example.com",
    "https://google.com",
    "http://192.168.1.1",
    "http://freemoneygiveaway.com"
]

for url in test_urls:
    is_phish, reason = is_phishing_url(url)
    print(f"URL: {url} -> Phishing: {is_phish} ({reason})")
