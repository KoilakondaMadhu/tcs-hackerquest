import re

def is_valid_ipv4(ip):
    # Regular expression to match valid IPv4 addresses
    ipv4_pattern = re.compile(r'^(\d{1,3}\.){3}\d{1,3}$')
    return ipv4_pattern.match(ip) is not None

def is_valid_ipv6(ip):
    # Regular expression to match valid IPv6 addresses
    ipv6_pattern = re.compile(r'^([0-9a-fA-F]{0,4}:){2,7}[0-9a-fA-F]{0,4}$')
    return ipv6_pattern.match(ip) is not None

def identify_malicious_ips(ip_list):
    malicious_ips = []
    for ip in ip_list:
        if ip.startswith("92.85.") and is_valid_ipv4(ip):
            malicious_ips.append(ip)
        elif re.match(r'^2510:a5:[0-9a-fA-F]{1,4}:[0-9a-fA-F]{1,4}:[0-9a-fA-F]{1,4}:[0-9a-fA-F]{1,4}$', ip):
            malicious_ips.append(ip)
    return malicious_ips

def extract_last_characters(malicious_ips):
    last_characters = []
    for ip in malicious_ips:
        last_characters.append(ip[-1])
    return ''.join(last_characters)

# Sample IP addresses file path
file_path = "ip_addresses.txt"

# Read IP addresses from file
with open(file_path, 'r') as file:
    ip_addresses = file.read().splitlines()

# Identify malicious IPs
malicious_ips = identify_malicious_ips(ip_addresses)

# Extract last characters of malicious IPs
flag = extract_last_characters(malicious_ips)

# Construct the flag
flag = "HQ8{" + flag + "}"

print("Flag:", flag)
