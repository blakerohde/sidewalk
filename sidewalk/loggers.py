"""
sidewalk.loggers

This module contains simple loggers for printing pretty messages.

:copyright: (c) 2012 by Blake Rohde.
:license: ISC, see LICENSE for more details.
"""

import time

def log(message, tag='GENERAL', verbose=False):
	"""Simple log/message function for the output of timestamped messages."""
	
	print '%s\t%s\t%s' % (
		time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()),
		tag,
		message
	)

def error(message):
	"""Error log wrapper for log."""
	
	log(message, tag='ERROR', verbose=True)

def debug(message):
	"""Debug log wrapper for log."""
	
	log(message, tag='DEBUG', verbose=True)
