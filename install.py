# =============================================================
# COPYRIGHT (C) 2026 tawfique02. ALL RIGHTS RESERVED.
# This software is proprietary. Redistribution or modification 
# of this code is strictly prohibited.
# =============================================================
import os
import sys

def install():
    print("--- Auto Tor IP Changer Installer ---")
    choice = input('[+] Press (Y) to Install or (N) to Uninstall >> ').lower()
    
    if choice == 'y':
        # Create directory in /usr/share
        os.system('sudo mkdir -p /usr/share/mytor')
        
        # এখানে tor.py এর বদলে mytor.py দেওয়া হয়েছে
        if os.path.exists('mytor.py'):
            os.system('sudo cp mytor.py /usr/share/mytor/tor.py')
        else:
            print("\033[1;31m[!] Error: 'mytor.py' not found in current directory!\033[0m")
            return

        # Create the launcher script in /usr/bin
        launcher_path = '/usr/bin/mytor'
        command = '#!/bin/bash\nexec python3 /usr/share/mytor/tor.py "$@"'
        
        try:
            with open('mytor_launcher', 'w') as f:
                f.write(command)
            
            os.system('sudo mv mytor_launcher ' + launcher_path)
            os.system('sudo chmod +x ' + launcher_path)
            os.system('sudo chmod +x /usr/share/mytor/tor.py')
            
            print("\n\033[1;32m[+] Installation successful!")
            print("[*] From now on, just type 'mytor' in any terminal.\033[0m")
        except Exception as e:
            print(f"[!] Error: {e}")
            
    elif choice == 'n':
        os.system('sudo rm -rf /usr/share/mytor')
        os.system('sudo rm /usr/bin/mytor')
        print("\033[1;31m[!] Tool uninstalled successfully.\033[0m")

if __name__ == "__main__":
    if os.geteuid() != 0:
        print("[!] Please run this installer with sudo.")
    else:
        install()
