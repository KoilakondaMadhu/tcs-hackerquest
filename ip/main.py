import pyshark
import os

# Function to analyze TLS traffic and search for the flag
def analyze_tls_traffic(pcap_file, ssl_key):
    # Load the network capture file
    capture = pyshark.FileCapture(pcap_file, decryption_key=ssl_key)

    # Iterate through each packet in the capture
    for packet in capture:
        # Check if the packet is a TLS handshake packet
        if 'TLS' in packet and 'handshake' in packet['TLS'].lower():
            # Check if the packet contains the flag
            if "HQ8{EnterHQ8KeyHere}" in str(packet):
                print("Flag found in TLS traffic:")
                print(packet)
                break

    capture.close()

# Main function
def main():
    # Get the current directory
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Provide the relative path to the network capture file (pcap)
    pcap_file = os.path.join(current_dir, "Baby_SharkDoDoDoDo.pcapng")

    # Provide the relative path to the SSL key file
    ssl_key = os.path.join(current_dir, "sslkey")

    # Analyze TLS traffic and search for the flag
    analyze_tls_traffic(pcap_file, ssl_key)

if __name__ == "__main__":
    main()
