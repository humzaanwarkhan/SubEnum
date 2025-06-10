# SubEnum
SubEnum is a simple yet effective Python-based subdomain enumeration tool designed for cybersecurity enthusiasts and bug bounty hunters. It helps you discover live subdomains of a target domain by resolving potential subdomains from a customizable wordlist and checking their HTTP status to identify active hosts.

Features:

1. Enumerates subdomains based on a user-provided wordlist
2. Resolves DNS to find IP addresses of subdomains
3. Checks HTTP availability (live or down) with status codes
4. Lightweight and easy to use from the command line
5. Provides a clean, professional banner with developer credit

Why SubEnum?
While many advanced tools like subfinder exist, SubEnum is built from scratch as a learning project to understand the fundamentals of DNS resolution, HTTP requests, and subdomain enumeration techniques. It’s a great starter project to showcase your skills in Python programming and basic cybersecurity reconnaissance.

Installation:

Make sure you have Python 3 installed along with the requests library:

```pip install requests```

Usage:

```python subenum.py -d example.com -w wordlist.txt```

-->  -d or --domain specifies the target domain.
-->  -w or --wordlist specifies the path to a file containing subdomain names (one per line).

Example:

```python subenum.py -d hackerone.com -w subdomains.txt```

How It Works

1. Reads subdomains from the given wordlist.
2. Appends each subdomain to the target domain (e.g., api.example.com).
3. Resolves the full domain to get its IP address using DNS lookup.
4. Sends a HTTP GET request to check if the subdomain is alive and captures the HTTP status code.
5. Prints live or down status with domain and IP address.

Contributing:

Contributions are welcome! Feel free to open issues or pull requests to improve SubEnum.

# -Developed by Humza Anwar Khan 


