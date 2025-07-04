# 🔍 Ping Sweep & Port Scanner (Python)

A simple Python script that performs two main tasks:
1. **Ping Sweep** — discovers live hosts on a given network.
2. **Port Scanning** — scans open ports on discovered hosts.

---

## 📦 Features

- Scans a full CIDR subnet (e.g. `192.168.1.0/24`)
- Detects live hosts by attempting socket connections on port 80
- Scans for open ports: 22 (SSH), 80 (HTTP), 443 (HTTPS)
- Uses multi-threading for fast scanning

---

## 🚀 Getting Started

### ▶️ Run the script

```bash
python3 ping_port_scan.py


Make sure to edit the network range in the script:
network = "192.168.1.0/24"  # Change this to match your local network


Example Output:
[~] Scanning network: 192.168.1.0/24
[+] Host is up: 192.168.1.5
[+] Host is up: 192.168.1.8
[+] Open port 22 on 192.168.1.5
[+] Open port 80 on 192.168.1.5
[+] Open port 443 on 192.168.1.8
