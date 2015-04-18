icmpKNOCK
=========

ICMP Port KNOCKing Tool

What's this about?lls
------------------

If you're familiar with port knocking, you should know the basics and how this 
technique basically works.

Most port knocking tools are listening for TCP or UDP packets to arrive on 
specific ports in a specific order. icmpKNOCK is waiting for ICMP echo requests
and checks their payloads. Packets that match given criteria trigger some 
action, e.g. open/close port(s) etc.

The main advantage of this tool is the fact that this approach works with all 
standard ping tools, regardless of your operating system.


How to use it
-------------
    a) Define some actions (check out icmpKNOCK.py for a sample action
    b) Add actions to listener
    c) run icmpKNOCK.py as root!!! otherwise you won't be able to listen
       for incoming ICMP requests
    d) Using your ping utility you can pass hex patterns to the requests:
       $ ping -p [hex pattern] [host]
