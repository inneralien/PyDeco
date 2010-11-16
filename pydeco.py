#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from optparse import OptionParser
import sys
import logging
import TestClass

__author__        = "Your Name Here"
__copyright__     = "Copyright: (C) 2010 <COMPANY_NAME>"
__creation_date__ = ":r!date"
__version__       = 'v0.1.0'


if __name__ == '__main__':
#==============================================================================
# Define logging levels for the command line
#==============================================================================
    LEVELS = {  'debug'    : logging.DEBUG,
                'info'     : logging.INFO,
                'warning'  : logging.WARNING,
                'error'    : logging.ERROR,
                'critical' : logging.CRITICAL,
            }

#==============================================================================
# Option Parser
#==============================================================================
    parser = OptionParser(usage="%prog <options> [filename]", version="%s\n%s" % (__version__, __copyright__))
    parser.add_option("-d", "--debug",
                        dest="debug",
                        default='error',
                        help="Run in special debug mode. Valid options are debug, info, warning, error, critical")
    parser.add_option("-l", "--long_messages",
                        default=False,
                        action='store_true',
                        dest="long_messages",
                        help="Print out extra help messages on warnings and errors")

    (options, args) = parser.parse_args()

    if(len(args) == 1):
        filename = args[0]
    else:
        parser.print_help()
        sys.exit(1)

#==============================================================================
# Turn on logging
#==============================================================================
    logging.basicConfig()
    logging.getLogger().setLevel(LEVELS[options.debug])


#==============================================================================
# Do stuff here
#==============================================================================
    stuff = TestClass.TestClass()
