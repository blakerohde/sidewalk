"""
sidewalk.activity_aggregator

This module is the primary workhorse powering Sidewalk. Let's execute some activity processors!

:copyright: (c) 2013 by Blake Rohde.
:license: ISC, see LICENSE for more details.
"""

import sys
import traceback

from sidewalk.core import exceptions, loggers
from sidewalk.core.manager import ActivityProcessorsManager


class ActivityAggregator:
    """The :class:`ActivityAggregator` object. It allows for the execution of the defined
    activity processors.
    """
    
    def __init__(self, filename=None, active_activity_processor_keys=[], active_group_keys=[]):
        self.settings_filename = filename
        self.manager = ActivityProcessorsManager(filename=self.settings_filename)
        
        self.active_activity_processor_pairs = self.manager.get_activity_processor_pairs(active_activity_processor_keys)
        
        for group_key in active_group_keys:
            self.active_activity_processor_pairs.update(self.manager.get_group_activity_processor_pairs(group_key))
    

    def import_module(self, name):
        """Simple wrapper for importing the requested module."""
        
        __import__(name)
        
        return sys.modules[name]
    

    def run(self):
        """The primary workhorse. Runs/executes the active activity processors."""
        
        loggers.debug('run():')
        
        # If no active activity processor pairs, process them all
        if len(self.active_activity_processor_pairs) == 0:
            self.active_activity_processor_pairs = self.manager.get_activity_processor_pairs()
        
        for (key, activity_processor) in self.active_activity_processor_pairs.items():  
            attr = activity_processor[activity_processor.rfind('.')+1:]
            path = activity_processor.split('.')[:-1]
            
            loggers.debug('callable: ' + attr)
            loggers.debug('location: %s' % path)
            
            # Try to import the module by importing module N-1 from the path (the Nth is the function/attr node of the path). If that doesn't work, try importing the submodule of the N-1 path and keep going util the base module.
            module, function = None, None
            
            for i in reversed(range(1, len(path)+1)):
                try:
                    loggers.debug('import \'' + '.'.join(path[:i]) + '\'?')
                    module = self.import_module('.'.join(path[:i]))
                    loggers.debug(module)
                except ImportError:
                    loggers.debug('no.')
                    loggers.debug(traceback.format_exc())
                    continue
                
                if module is not None:
                    while True:
                        try:
                            loggers.debug('sub-import \'' + '.'.join(path[1:i+1]) + '\'?')
                            tmp = getattr(module, '.'.join(path[1:i+1]))
                            module = tmp
                            loggers.debug('yes.')
                        except AttributeError:
                            loggers.debug('no.')
                            #loggers.debug(traceback.format_exc())
                            break
                    
                    if module is not None:
                        try:
                            loggers.debug('get attr \'' + attr + '\' in ' + str(module) + '?')
                            function = getattr(module, attr)
                            loggers.debug('yes.')
                            break
                        except AttributeError:
                            loggers.debug('no.')
                            loggers.debug(traceback.format_exc())
            
            # Execute the function
            if function is not None:
                loggers.debug('running...')
                function()
            else:
                raise exceptions.SidewalkMethodDoesNotExist(module='.'.join(path), method=attr)
