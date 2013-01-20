"""
sidewalk.exceptions

This module contains custom exceptions that can be thrown by Sidewalk.

:copyright: (c) 2013 by Blake Rohde.
:license: ISC, see LICENSE for more details.
"""


class SidewalkSettingsFileIOError(Exception):
	"""Settings file IOError."""
	
	def __init__(self, filename, permission):
		self.filename = filename
		self.permission = permission
	

	def __str__(self):
		return repr('%s %s' % (
			self.filename,
			self.permission
		))


class SidewalkSectionNotDefined(Exception):
	"""The specified settings file does not contain a required section."""
	
	def __init__(self, filename, section):
		self.filename = filename
		self.section = section
	

	def __str__(self):
		return repr('%s %s' % (
			self.filename,
			self.section
		))


class SidewalkKeyDoesNotExist(Exception):
	"""Activity processor requested is not defined."""
	
	def __init__(self, key):
		self.key = key
	

	def __str__(self):
		return repr(self.key)


class SidewalkGroupDoesNotExist(Exception):
	"""Activity processor group requested is not defined."""
	
	def __init__(self, group_key):
		self.group_key = group_key
	

	def __str__(self):
		return repr(self.group_key)


class SidewalkModuleImportError(Exception):
	"""Activity processor module could not be imported."""
	
	def __init__(self, module):
		self.module = module
	

	def __str__(self):
		return repr(self.module)


class SidewalkMethodDoesNotExist(Exception):
	"""The Activity processor (method) does exist in the specified module."""
	
	def __init__(self, module, method):
		self.module = module
		self.method = method
	

	def __str__(self):
		return repr('%s %s' % (
			self.module,
			self.method
		))


class SidewalkRogueActivityProcessor(Exception):
	"""The Activity processor threw an unhandled exception."""
	
	def __init__(self, activity_processor):
		self.activity_processor = activity_processor
	

	def __str__(self):
		return repr(self.activity_processor)
