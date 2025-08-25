from scapy.all import TCP, sniff, IP, UDP, ICMP, DNS, DNSQR
from folder_1 import logger

logger = logger("my_scapy")
IFACE = None
BPF = "tcp or udp or icmp or port 53"

def on_puket(pkt):
    if IP not in pkt:
        return
    
    if IP in pkt and TCP in pkt:
        src = pkt[IP].src 
        dst = pkt[IP].dst
        logger.info(f"TCP {src}:{pkt[TCP].sport} -> {dst}:{pkt[TCP].dport}")

    elif UDP in pkt:
        if DNS in pkt and DNSQR in pkt and pkt[DNS].qd:
            qname = pkt[DNS].qd.qname.decode(errors="ignore")
            logger.info(f"DNS  {src}:{pkt[UDP].sport} -> {dst}:{pkt[UDP].dport}  q={qname}")
        else:
            logger.info(f"UDP  {src}:{pkt[UDP].sport} -> {dst}:{pkt[UDP].dport}")

    elif ICMP in pkt:
        print(f"ICMP {src} -> {dst} type={pkt[ICMP].type} code={pkt[ICMP].code}")


logger.info(f"Sniffing iface={IFACE or 'default'} filter={BPF}")
sniff(filter=BPF, prn=on_puket, store=False, iface=IFACE)
