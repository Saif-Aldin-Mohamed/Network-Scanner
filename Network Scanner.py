import socket
import ipaddress
from concurrent.futures import ThreadPoolExecutor

# ----------------------------
# Configurations
# ----------------------------
network = "192.168.1.0/24"  # Modify this to match your network
ports_to_scan = [22, 80, 443]
thread_count = 50
timeout = 1

# ----------------------------
# Scan one port on a host
# ----------------------------
def scan_port(ip, port):
    try:
        with socket.socket() as sock:
            sock.settimeout(timeout)
            sock.connect((ip, port))
            print(f"[+] Open port {port} on {ip}")
    except:
        pass

# ----------------------------
# Ping host by attempting connection to port 80
# ----------------------------
def is_host_up(ip):
    try:
        with socket.socket() as sock:
            sock.settimeout(0.5)
            sock.connect((str(ip), 80))
            return True
    except:
        return False

# ----------------------------
# Sweep network for live hosts
# ----------------------------
def ping_sweep(network_range):
    print(f"[~] Performing ping sweep on {network_range}")
    live_hosts = []
    for ip in ipaddress.IPv4Network(network_range):
        if is_host_up(ip):
            print(f"[+] Host is up: {ip}")
            live_hosts.append(str(ip))
    return live_hosts

# ----------------------------
# Perform port scanning on list of IPs
# ----------------------------
def port_scan_all(live_hosts):
    print(f"[~] Scanning ports on {len(live_hosts)} live host(s)...")
    with ThreadPoolExecutor(max_workers=thread_count) as executor:
        for ip in live_hosts:
            for port in ports_to_scan:
                executor.submit(scan_port, ip, port)

# ----------------------------
# Main Execution
# ----------------------------
if __name__ == "__main__":
    live_hosts = ping_sweep(network)
    if live_hosts:
        port_scan_all(live_hosts)
    else:
        print("[-] No live hosts found.")
