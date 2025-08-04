import os
import sys
import time
from collections import defaultdict
from scapy.all import sniff,IP

THRESHOLD = 40
print(f"THRESHOLD: {THRESHOLD}")

def packet_callback(packet):
    src_ip = packet[IP].src
    packet_count[src_ip] += 1

    current_time = time.time()
    time_interval = current_time - start_time[0]

    if time_interval >= 1:
        for ip, count in packet_count.items():
            packet_rate = count / time_interval
            print(f"IP: {ip}, Packets: {count}, Rate: {packet_rate:.2f} packets/sec")
            if count > THRESHOLD:
                print(f"Potential DDoS attack detected from {ip} with {count} packets.")
                os.system(f"iptables -A INPUT -s {ip} -j DROP")
                blocked_ips.add(ip)
        packet_count.clear()
        start_time[0] = current_time

if __name__ == "__main__":
    if os.geteuid() != 0:
        print("Please run as root.")
        sys.exit(1)

    packet_count = defaultdict(int)
    start_time = [time.time()]
    blocked_ips = set()

    print("Monitoring network traffic ...")
    sniff(filter="ip", prn=packet_callback)