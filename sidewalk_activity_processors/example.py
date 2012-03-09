"""
sidewalk_activity_processors.example

This module contains sample activity processors.
"""

import sidewalk.loggers

def hello():
	"""Simply print hello world back to the console."""
	
	sidewalk.loggers.log('hello world')

def import_test():
	"""Import the core sidewalk module to check against a defined value."""
	
	import sidewalk
	sidewalk.loggers.debug('sidewalk == %s' % (sidewalk.__title__))

def baddie_unhandled_test():
	"""A test activity processor that throws an uncaught exception."""
	
	foo = ()
	foo[1] # should throw an IndexError exception
