"""
sidewalk_activity_processors.example

This module contains sample activity processors.
"""

def hello():
	"""Simply print hello world back to the console."""
	
	print 'hello world'

def import_test():
	"""Import the core sidewalk module to check against a defined value."""
	
	import sidewalk
	print 'sidewalk == %s' % (sidewalk.__title__)

def baddie_unhandled_test():
	"""A test activity processor that throws an uncaught exception."""
	
	foo = ()
	foo[1] # should throw an IndexError exception