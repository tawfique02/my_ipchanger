# 🛡️ Advanced Auto Tor IP Changer (v2.2)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)
![License](https://img.shields.io/badge/License-All%20Rights%20Reserved-red)
![OS](https://img.shields.io/badge/OS-Linux%20%2F%20Kali-red?logo=linux)

**Advanced Auto Tor IP Changer** is a professional-grade script designed for cybersecurity enthusiasts and researchers to automate IP rotation. It ensures anonymity by cycling through Tor exit nodes and verifying each new identity's geo-location.

---

## 🚀 Key Features
- ✅ **Automatic IP Rotation:** Set your own custom intervals (in seconds).
- ✅ **Geo-Location Intelligence:** Displays real-time IP, Country Code, and Country Name.
- ✅ **Infinite Mode:** Run the tool indefinitely or set a specific number of rotations.
- ✅ **Secure DNS Handling:** Uses SOCKS5h to prevent DNS leaks at the local level.
- ✅ **Session Logging:** Keeps a detailed record of every IP used in `tor_history.txt`.
- ✅ **One-Command Install:** Easy installation script for system-wide access.

---

## 🛠️ Installation & Setup

### 1. Prerequisites
Ensure you have the Tor service installed on your Linux machine:
```bash
sudo apt update && sudo apt install tor -y
```
2. Clone & Install
```Bash
git clone https://github.com/tawfique02/my_ipchanger.git
cd my_ipchanger
sudo python3 install.py
```
3. Usage
After installation, you can run the tool from anywhere in your terminal:

```Bash
sudo mytor
```
### 🌐 How to Route Browser Traffic
Simply running the script changes the Tor service IP, but your browser needs to be told to use that service. Follow these steps for Firefox:

Open Firefox Settings and search for Proxy.

Click Settings under "Network Settings".

Configure as follows:

Selection: Manual proxy configuration.

SOCKS Host: 127.0.0.1

Port: 9050

SOCKS Type: SOCKS v5

Crucial: Check the box "Proxy DNS when using SOCKS v5".

### 📊 How It Works
The script interacts with the Tor Control Port. When the timer hits, it sends a RELOAD or NEWNYM signal, forcing the Tor network to build a new circuit for your connection.

### 📂 Project Structure
```Plaintext
.
├── mytor.py           # The core engine (Logic)
├── install.py       # System-wide installer
├── tor_history.txt  # Auto-generated IP logs
└── README.md        # Documentation
```
## 📜 License
This project is protected under a **Custom Proprietary License**. 
All rights reserved by **tawfique02**. 

- 🚫 No Modification 
- 🚫 No Redistribution 
- ✅ Personal Use Only 

### 📜 Disclaimer
This tool is for Educational Purposes Only. Misuse of this tool for illegal activities is strictly prohibited. The developer is not responsible for any damage caused.


