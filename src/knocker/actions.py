"""
Actions are passed to the ICMPknock instance to define 
sequences and the action to complete after that sequence.
"""

import logging
from helpers import standard_knock_check

logger = logging.getLogger(__name__)

class Action(object):
    #:type: set
    sequence = None
    # action function
    action = None
    # friendly name (logger)
    name = None
    
    
    def __init__(self,**kwargs):
        self.action = kwargs.get('action')
        self.sequence = kwargs.get('sequence')
        self.name = kwargs.get('name')
        if self.name:
            self.__name__ = self.name 
    
    
    def knock(self,ip_address,knocks):
        """
        Checks the incoming knocks against the sequence
        If they match, executes the action.
        """
        if standard_knock_check(knocks):
            logger.info('opening door for {}'.format(ip_address))
            self.action(ip_address)
            
            