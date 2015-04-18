#!/usr/bin/env python
"""
 (_) ___ _ __ ___  _ __ | |/ / \ | |/ _ \ / ___| |/ /   
 | |/ __| '_ ` _ \| '_ \| ' /|  \| | | | | |   | ' /    
 | | (__| | | | | | |_) | . \| |\  | |_| | |___| . \    
 |_|\___|_| |_| |_| .__/|_|\_\_| \_|\___/ \____|_|\_\   
                  |_| (c) by Victor Dorneanu

icmpKNOCK - ICMP port knocking server
Copyright (C) 2009-2010 by Victor Dorneanu

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
"""
import logging
from knocker.listener import ICMPListener
from knocker.actions import Action

logging.basicConfig()
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


if __name__ == '__main__':

    log_action_secret = [ 'c7533ff6fabc19816a2d816941fa5f56',
                              'fafe47632b2a5e0a8b5fe2e8406b970b',
                              'f28dff849929fb5d43629328c23df1c1',
                              'b96276ed3de61330494eb201a3cb7fa7']
    
    def log_action_open_door(ip_address):
        """
        The function executed when the sequence is found
        """
        logger.error('successful knock from IP:{}'.format(ip_address))
        
        
    log_action = Action(sequence = log_action_secret,
                        name = 'log_action',
                        action = log_action_open_door)


    # Activate ICMP listener
    listener = ICMPListener(actions=[log_action])
    listener.go()
