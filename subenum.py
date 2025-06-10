import socket
import argparse
import requests

def print_banner():
    banner = r"""
███████╗██╗   ██╗██████╗ ███████╗███╗   ██╗██╗   ██╗███╗   ███╗
██╔════╝██║   ██║██╔══██╗██╔════╝████╗  ██║██║   ██║████╗ ████║
███████╗██║   ██║██████╔╝█████╗  ██╔██╗ ██║██║   ██║██╔████╔██║
╚════██║██║   ██║██╔══██╗██╔══╝  ██║╚██╗██║██║   ██║██║╚██╔╝██║
███████║╚██████╔╝██████╔╝███████╗██║ ╚████║╚██████╔╝██║ ╚═╝ ██║
╚══════╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝
                                                               
       -Developed by Humza Anwar Khan
"""
    print(banner)

def resolve_subdomain(domain, subdomain):
    full_domain = f"{subdomain}.{domain}"
    try:
        ip = socket.gethostbyname(full_domain)
        return (full_domain, ip)
    except socket.gaierror:
        return None

def check_http(url):
    try:
        response = requests.get(url, timeout=3)
        if 200 <= response.status_code < 400:
            return True, response.status_code
        else:
            return False, response.status_code
    except requests.RequestException:
        return False, None

def main():
    print_banner()
    
    parser = argparse.ArgumentParser(description="Simple Subdomain Enumerator with HTTP check")
    parser.add_argument("-d", "--domain", required=True, help="Target domain (e.g., example.com)")
    parser.add_argument("-w", "--wordlist", required=True, help="Path to subdomain wordlist")
    args = parser.parse_args()

    with open(args.wordlist, "r") as file:
        subdomains = file.read().splitlines()

    print(f"\n[+] Enumerating subdomains for: {args.domain}\n")

    for sub in subdomains:
        result = resolve_subdomain(args.domain, sub)
        if result:
            full_domain, ip = result
            url = f"http://{full_domain}"
            alive, status = check_http(url)
            if alive:
                print(f"[+] LIVE: {full_domain} ({ip}) [HTTP {status}]")
            else:
                print(f"[-] DOWN: {full_domain} ({ip})")

    print("\n[+] Enumeration completed! All subdomains checked.\n")

if __name__ == "__main__":
    main()
