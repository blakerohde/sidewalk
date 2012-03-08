"""
sidewalk

:copyright: (c) 2012 by Blake Rohde.
:license: ISC, see LICENSE for more details.
"""

import time

__title__ = 'sidewalk'
__version__ = '0.1.0'
__author__ = 'Blake Rohde'
__license__ = 'ISC'
__copyright__ = 'Copyright 2012 Blake Rohde'

def log(message, tag='GENERAL', verbose=False):
	"""Simple log/message function for the output of timestamped messages."""
	print '%s\t%s\t%s' % (
		time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()),
		tag,
		message
	)
	
def error_log(message):
	"""Error log wrapper for log."""
	log(message, tag='ERROR', verbose=True)
	
def debug_log(message):
	"""Debug log wrapper for log."""
	log(message, tag='DEBUG', verbose=True)