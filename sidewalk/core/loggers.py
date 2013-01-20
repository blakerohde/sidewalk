"""
sidewalk.loggers

This module contains simple loggers for printing pretty messages.

:copyright: (c) 2013 by Blake Rohde.
:license: ISC, see LICENSE for more details.
"""

import time

from sidewalk.conf import global_settings


def log(message, tag='GENERAL', verbose=False):
    """Simple log/message function for the output of timestamped messages."""
    
    if verbose:
        print '%s\t%s\t%s' % (
            time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()),
            tag,
            message
        )


def error(message, verbose=True):
    """Error log wrapper for log."""
    
    if verbose is None:
        verbose = global_settings.VERBOSE
    
    return log(message, tag='ERROR', verbose=verbose)


def debug(message, verbose=False):
    """Debug log wrapper for log."""
    
    if verbose is None:
        verbose = global_settings.VERBOSE
    
    log(message, tag='DEBUG', verbose=verbose)
