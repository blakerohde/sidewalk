"""
sidewarlk.test.example

This module contains sample activity processors.
"""

from sidewalk.core import loggers


def hello():
    """Simply print hello world back to the console."""
    
    loggers.debug('hello world', verbose=True)


def import_test():
    """Import the core sidewalk module to check against a defined value."""
    
    import sidewalk
    loggers.debug('sidewalk == %s' % (sidewalk.__title__), verbose=True)


def baddie_unhandled_test():
    """A test activity processor that throws an uncaught exception."""
    
    foo = ()
    foo[1] # should throw an IndexError exception
