"""
 (_) ___ _ __ ___  _ __ | |/ / \ | |/ _ \ / ___| |/ /   
 | |/ __| '_ ` _ \| '_ \| ' /|  \| | | | | |   | ' /    
 | | (__| | | | | | |_) | . \| |\  | |_| | |___| . \    
 |_|\___|_| |_| |_| .__/|_|\_\_| \_|\___/ \____|_|\_\   
                  |_| (c) by Victor Dorneanu

icmpKNOCK - ICMP port knocking server
Copyright (C) 2009-2010 by Victor Dorneanu
"""


""" Provide several utilities like debug messages etc. """


def show_debug_msg(where, msg):
    """ Print debug message <msg> to the standard output """
    print ">> [%s] %s " % (where, msg)


def whoami(obj=None):
    import sys
    if obj:
        return class_name(obj) + " :: " + sys._getframe(1).f_code.co_name
    else:
        return sys._getframe(1).f_code.co_name


def class_name(obj):
    return obj.__class__.__name__

