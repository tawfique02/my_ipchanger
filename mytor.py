# -*- coding: utf-8 -*-
import time
import os
import requests
from datetime import datetime

# Check and install dependencies
try:
    import requests
except ImportError:
    print('[+] "requests" library not found. Installing...')
    os.system('pip3 install requests requests[socks]')

def get_ip_info():
    """Fetches IP, Country Name, and Country Code through Tor."""
    url = 'http://ip-api.com/json/'
    proxies = {
        'http': 'socks5h://127.0.0.1:9050',
        'https': 'socks5h://127.0.0.1:9050'
    }
    try:
        response = requests.get(url, proxies=proxies, timeout=10).json()
        if response.get('status') == 'success':
            ip = response.get('query')
            country = response.get('country')
            code = response.get('countryCode')
            data = f"{ip} [{code} - {country}]"
            
            # Log to file
            with open("tor_history.txt", "a") as log:
                now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                log.write(f"[{now}] {data}\n")
                
            return data
        else:
            return "Unable to fetch location data."
    except Exception:
        return "\033[1;31mConnection Error! (Is Tor running?)\033[0m"

def change_ip():
    """Reloads Tor service and prints the new IP with Country details."""
    os.system("sudo service tor reload")
    time.sleep(3) 
    info = get_ip_info()
    print(f'\033[1;32m[+] IP Successfully Changed to: {info} ✅\033[0m')

def banner():
    print('''\033[1;34m
    ===========================================
    |        PERSONAL AUTO TOR CHANGER        |
    |          Developer: tawfique02          |
    ===========================================\033[0m''')

def main():
    os.system("clear")
    banner()
    
    print("[*] Starting Tor service...")
    os.system("sudo service tor start")
    time.sleep(2)
    
    print("\033[1;33m[!] Set your application SOCKS proxy to 127.0.0.1:9050\033[0m\n")
    
    try:
        # Fixed: Calling get_ip_info() instead of get_ip()
        print(f"[*] Checking initial connection...")
        print(f"\033[1;32m[+] Initial IP: {get_ip_info()}\033[0m")
        
        sec = int(input("[+] Change IP every (seconds) [Default: 60] >> ") or "60")
        times = int(input("[+] How many times? (0 for Infinite) >> ") or "0")
        
        count = 0
        if times == 0:
            print("[*] Running in Infinite mode. Press Ctrl+C to stop.")
            while True:
                time.sleep(sec)
                change_ip()
        else:
            for _ in range(times):
                time.sleep(sec)
                change_ip()
                count += 1
            print(f"\n[+] Task completed. Changed IP {count} times.")
            print("[*] Check 'tor_history.txt' for the full list of IPs.")
                
    except KeyboardInterrupt:
        print('\n\033[1;31m[!] Tool stopped by user.\033[0m')
    except ValueError:
        print("[!] Invalid input! Please enter numbers only.")

if __name__ == "__main__":
    main()
