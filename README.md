# Phishing-URL-Detector
Overview

The Phishing URL Detector is a Python-based cybersecurity tool designed to analyze website URLs and identify potential phishing threats. By detecting suspicious patterns, keywords, and domain structures, this tool helps in mitigating phishing attacks before users fall victim to them.

Features

Domain Analysis: Extracts and evaluates domain names for suspicious indicators.

IP-based URL Detection: Flags URLs that use raw IP addresses instead of domain names, a common phishing tactic.

Keyword Detection: Identifies dangerous words like login, bank, verify, secure, free, etc.

URL Length Analysis: Flags unusually long URLs that might be used to obscure phishing attempts.

Scalability: Can analyze multiple URLs quickly.

How It Works

The user provides a URL.

The tool extracts the domain and scans for:

Suspicious keywords

Unusual length

IP-based structures

The tool then outputs a warning if the URL matches phishing patterns.

Technologies Used

Python (Core language)

Regular Expressions (Regex) (For pattern detection)

urllib.parse (For URL parsing and domain extraction)

