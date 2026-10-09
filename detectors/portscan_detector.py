from scapy.all import rdpcap

packets = rdpcap("../captures/scan_portscan.pcapng") 
print("Total packets:", len(packets))
