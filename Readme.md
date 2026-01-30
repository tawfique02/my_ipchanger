<h1 align="center">🛡️ Advanced Auto Tor IP Changer (v2.2)</h1>
<p align="center">
  <img src="https://raw.githubusercontent.com/tawfique02/my_ipchanger/main/mage_d883wud883wud883.png" alt="Auto Tor IP Changer Banner" width="700">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue?logo=python" alt="Python">
  <img src="https://img.shields.io/badge/License-All%20Rights%20Reserved-red" alt="License">
  <img src="https://img.shields.io/badge/OS-Linux%20%2F%20Kali-red?logo=linux" alt="OS">
</p>

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
pip3 install -r requirements.txt --break-system-packages
sudo python3 install.py
```
3. Usage
After installation, you can run the tool from anywhere in your terminal:

```Bash
sudo mytor
```
### 🌐 How to Route Browser Traffic

Simply running the script changes the Tor service IP, but your browser needs to be told to use that service. Follow these steps for **Firefox**:

1.  Open **Firefox Settings** and search for **Proxy**.
2.  Click **Settings** under **"Network Settings"**.
3.  Configure as follows:
    * **Selection:** Manual proxy configuration.
    * **SOCKS Host:** `127.0.0.1`
    * **Port:** `9050`
    * **SOCKS Type:** SOCKS v5
    * **Crucial:** Check the box **"Proxy DNS when using SOCKS v5"**.

---

### 📸 Configuration Screenshot
<p align="center">
  <img src="https://raw.githubusercontent.com/tawfique02/my_ipchanger/main/Screenshot%202026-01-30%20200655.png" alt="Firefox Proxy Setup" width="700">
</p>

---

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
All rights reserved ❤️ by [**tawfique02**](https://github.com/tawfique02). 

- 🚫 No Modification 
- 🚫 No Redistribution 
- ✅ Personal Use Only 
---
## 🔍 Verify Your Anonymity
Before starting the rotation, it is highly recommended to verify if your browser is correctly routed through the Tor network.

1.  **Tor Check:** [check.torproject.org](https://check.torproject.org/) - To see if you are using Tor.
2.  **DNS Leak Test:** [dnsleaktest.com](https://www.dnsleaktest.com/) - To ensure your real IP is not leaking through DNS.

### 📜 Disclaimer
This tool is for Educational Purposes Only. Misuse of this tool for illegal activities is strictly prohibited. The developer is not responsible for any damage caused.


