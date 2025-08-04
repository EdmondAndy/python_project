import random

def generate_random_ip():
    """Generate a random IP address."""
    return f"192.168.1.{random.randint(1, 20)}"

def check_firewall_rules(ip, rules):
    """Check if the IP address matches any firewall rule and return the action."""
    for rule_ip, action in rules.items():
        if ip == rule_ip:
            return action
    return "allow"  

def main():
    # Define the firewall rules (key: IP address, value: action)
    firewall_rules = {
        "192.168.1.1": "block",
        "192.168.1.2": "block",
        "192.168.1.3": "block",
        "192.168.1.4": "block",
        "192.168.1.5": "block"
    }

    for _ in range(12):
        ip_address = generate_random_ip()
        action = check_firewall_rules(ip_address, firewall_rules)
        random_number = random.randint(1, 9999)
        print(f"IP: {ip_address}, Action: {action}, Random Number: {random_number}")

if __name__ == "__main__":
    main()



# Output example:
# IP: 192.168.1.13, Action: allow, Random Number: 1361
# IP: 192.168.1.16, Action: allow, Random Number: 4529
# IP: 192.168.1.15, Action: allow, Random Number: 4726
# IP: 192.168.1.2, Action: block, Random Number: 210
# IP: 192.168.1.1, Action: block, Random Number: 4245
# IP: 192.168.1.12, Action: allow, Random Number: 6847
# IP: 192.168.1.5, Action: block, Random Number: 7249
# IP: 192.168.1.5, Action: block, Random Number: 5058
# IP: 192.168.1.15, Action: allow, Random Number: 8907
# IP: 192.168.1.16, Action: allow, Random Number: 356
# IP: 192.168.1.16, Action: allow, Random Number: 6369
# IP: 192.168.1.20, Action: allow, Random Number: 5481