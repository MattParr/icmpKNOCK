"""
 (_) ___ _ __ ___  _ __ | |/ / \ | |/ _ \ / ___| |/ /   
 | |/ __| '_ ` _ \| '_ \| ' /|  \| | | | | |   | ' /    
 | | (__| | | | | | |_) | . \| |\  | |_| | |___| . \    
 |_|\___|_| |_| |_| .__/|_|\_\_| \_|\___/ \____|_|\_\   
                  |_| (c) by Victor Dorneanu

icmpKNOCK - ICMP port knocking server
Copyright (C) 2009-2010 by Victor Dorneanu
"""

import logging
import socket
import time
from helpers import get_packet_payload, get_packet_saddr

logger = logging.getLogger(__name__)

# seconds to allow between knocks
MAX_KNOCK_DELAY = 5
# max number of knocks that can make up a knock code
MAX_NUM_KNOCKS = 4
# min number of knocks that can make up a knock code
MIN_NUM_KNOCKS = 4

# --- Listen for ICMP packets 
class ICMPListener(object):
    
    def __init__(self, **kwargs):
        """
             Servers constructor
             * Set actions, port knock delay etc.
             * Create socket to listen for ICMP requests
        """
        self.actions = kwargs.get('actions',list())
        
        self.knock_timer = dict()
        self.knocks = dict()
        # Open socket (requires roOt)
        # TODO: if id != 0 then exit
        logger.debug( "Creating listening socket (AF_INET, SOCK_RAW, IPPROTO_ICMP)" )
        self.sock = socket.socket(socket.AF_INET,
                                  socket.SOCK_RAW,
                                  socket.IPPROTO_ICMP)
        self.sock.bind(('', 1))


    def go(self):
        """ Receive and process a requests """
        logger.debug( "Listening for incoming packets ..." )
        while True:
            try:
                data = self.sock.recv(1024)
            except socket.error:
                print "Can't receive packet"
                raise
            self.process_packet(data)


    def process_knock(self,payload,ip_address):
        # get the current knocks for this IP address
        knocks = self.knocks.setdefault(ip_address,set())
        # Check for knock delay 
        now = time.time()
        last_knock = self.knock_timer.get(ip_address,now)
        # if the timer has expired... forget the previous knocks
        if now > (last_knock + MAX_KNOCK_DELAY):
            # this knock becomes the first knock
            logger.debug('{} reset knocks: timer expired'.format(ip_address))
            knocks.clear()
        # if adding this knock would take the IP_address over the knock limit
        # this knock becomes the first knock
        if len(knocks) == MAX_NUM_KNOCKS:
            logger.debug('{} reset knocks: max knock limit reached'.format(ip_address))
            knocks.clear()
        # add this knock to the list
        knocks.add(payload)
        # update the timer for this knock
        self.knock_timer[ip_address] = now
        # process the knocks
        self.process_knocks(ip_address, knocks)
        
        
    def process_packet(self, packet):
        """ 
        Check if packet contains our keys 
        TODO: change the store so we are filtering sequences by source address
        otherwise we can't handle multiple knocks
        """
        payload = get_packet_payload(packet)
        ip_address = get_packet_saddr(packet)
        logger.debug('packet payload:{}:{}'.format(ip_address,payload))
        self.process_knock(payload,ip_address)
            
        
    def process_knocks(self, ip_address, knocks):
        """
        check the knocks against actions
        """
        # nothing to process, so return
        if len(knocks) < MIN_NUM_KNOCKS:
            logger.debug('{} {} is not enough knocks'.format(ip_address,len(knocks)))
            return
        
        for action in self.actions:
            action.knock(ip_address,knocks)
            
        
    def add_action(self,action):
        self.actions.append(action)

