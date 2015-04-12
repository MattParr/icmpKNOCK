"""
 (_) ___ _ __ ___  _ __ | |/ / \ | |/ _ \ / ___| |/ /   
 | |/ __| '_ ` _ \| '_ \| ' /|  \| | | | | |   | ' /    
 | | (__| | | | | | |_) | . \| |\  | |_| | |___| . \    
 |_|\___|_| |_| |_| .__/|_|\_\_| \_|\___/ \____|_|\_\   
                  |_| (c) by Victor Dorneanu

icmpKNOCK - ICMP port knocking server
Copyright (C) 2009-2010 by Victor Dorneanu
"""
from struct import unpack
from socket import inet_ntoa

def get_packet_saddr(packet):
    """
    Parse the packet IP headers and return source IP address
    """
    # Split packet into IP header and data (RFC 791) (ends at 20)
    # unpack the headers which gives src ip at index 8
    # unpack the binary representation to string
    return inet_ntoa(unpack('!BBHHHBBH4s4s' , packet[0:20])[8])
    
    
def get_packet_payload(data):
    """
    Parse packet and return HEX string specific to ICMPKnock
    """
    # Split packet into IP header and data (RFC 791) (starts at 20)
    # Split IP data into ICMP header and ICMP data (RFC 792) (starts at 20, goes for 8 - for our data)
    # Return payload data as hex string representation
    return ''.join( [ "%02x" % ord( x ) for x in data[20:28] ] ).strip()


def standard_knock_check(codes,knocks):
    """
    Compare codes with knocks (these are sets)
    """
    doorman_code = ''.join(codes)
    knock_code = ''.join(knocks)
    if doorman_code == knock_code:
        return True
    return False