from random import randint, choice
from scapy.all import *

def icmp_traffic(ip,i):
    icmp_packet = IP(dst=ip)/ICMP()
    send(icmp_packet, count=i)

def tcp_traffic(ip,i):
    multiplier = randint(100,10000)
    data = 'A' * multiplier
    ## Maybe import text file and encode it to send instead of A's
    tcp_traffic= IP(dst=ip)/TCP(sport=135, dport=5000) / Raw(load=data)
    send(tcp_traffic, count=i)

if __name__ == "__main__":
    for i in range(0,15):
        count1 = randint(1,10)
        count2 = randint(1,1000)
        count = count1*count2
        choice = randint(0,5)
        ## Read in a list of IPs to be more efficient
        ip = ['10.10.10.10']

        icmp_traffic(choice(ip), count)
        count1 = randint(1,10)
        count2 = randint(1,1000)
        count = count1*count2
        tcp_traffic(choice(ip), count)
        print "hello"
