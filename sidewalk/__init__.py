"""
sidewalk

:copyright: (c) 2012 by Blake Rohde.
:license: ISC, see LICENSE for more details.
"""

import os

__title__ = 'sidewalk'
__version__ = '0.0.1'
__author__ = 'Blake Rohde'
__license__ = 'ISC'
__copyright__ = 'Copyright 2012 Blake Rohde'

__root_dir = os.path.abspath(os.path.dirname(__file__))
def get_conf(path):
	"""Get the path of the requested configuration file."""
	
	return os.path.join(__root_dir, 'conf', path)