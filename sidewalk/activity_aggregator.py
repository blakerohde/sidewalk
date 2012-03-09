"""
sidewalk.activity_aggregator

This module is the primary workhorse powering Sidewalk. Let's execute some activity processors!

:copyright: (c) 2012 by Blake Rohde.
:license: ISC, see LICENSE for more details.
"""

import string
import sys

import sidewalk
import sidewalk.manager
import sidewalk.exceptions
from sidewalk.manager import ActivityProcessorsManager

class ActivityAggregator:
	"""The :class:`ActivityAggregator` object. It allows for the execution of the defined
	activity processors.
	"""
	
	def __init__(self, filename=None, active_activity_processor_keys=[], active_group_keys=[], verbose=False):
		self.settings_filename = filename
		self.manager = ActivityProcessorsManager(filename=self.settings_filename)
		
		self.verbose = verbose
		self.active_activity_processor_pairs = self.manager.get_activity_processor_pairs(active_activity_processor_keys)
		
		for group_key in active_group_keys:
			self.active_activity_processor_pairs.update(self.manager.get_group_activity_processor_pairs(group_key))
	
	def import_module(self, name):
		"""Simple wrapper for importing the requested module."""
		
		__import__(name)
		
		return sys.modules[name]
	
	def run(self):
		"""The primary workhorse. Runs/executes the active activity processors."""
		
		# If no active activity processor pairs, process them all
		if len(self.active_activity_processor_pairs) == 0:
			self.active_activity_processor_pairs = self.manager.get_activity_processor_pairs()
		
		for (key, activity_processor) in self.active_activity_processor_pairs.items():	
			i = activity_processor.rfind('.')
			module, attr = activity_processor[:i], activity_processor[i+1:]
			
			try:
				mod = self.import_module(module)
			except ImportError:
				raise sidewalk.exceptions.SidewalkModuleImportError(module=module)
			
			try:
				func = getattr(mod, attr)
			except AttributeError:
				raise sidewalk.exceptions.SidewalkMethodDoesNotExist(module=module, method=attr)
			
			try:
				func()
			except:
				raise sidewalk.exceptions.SidewalkRogueActivityProcessor(activity_processor=activity_processor)
