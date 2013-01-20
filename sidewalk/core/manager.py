"""
sidewalk.manager

This module contains manager(s) for managing Sidewalk resources (setting files, etc.).

:copyright: (c) 2013 by Blake Rohde.
:license: ISC, see LICENSE for more details.
"""

import os
import string
import ConfigParser

from sidewalk.core import exceptions


class ActivityProcessorsManager:
    """The :class:`ActivityProcessorsManager` object. It allows for the management and storage of
    activity processors defined in the primary settings.conf config file.
    """
    
    def __init__(self, filename=None):
        self.__filename = filename
        self.__activity_processor_pairs = None
        self.__config = ConfigParser.ConfigParser()
        
        if self.__filename != None:
            self.open(self.__filename)
    

    def open(self, filename):
        """Open the specified configuration file."""
        
        self.__filename = filename
        
        try:
            self.__config.readfp(open(self.__filename, 'r'))
        except IOError:
            raise exceptions.SidewalkSettingsFileIOError(filename=self.__filename, permission='r')
        
        try:
            self.__activity_processor_pairs = dict(self.__config.items('activity_processors'))
        except ConfigParser.NoSectionError:
            raise exceptions.SidewalkSectionNotDefined(filename=self.__filename, section='activity_processors')
    

    def save(self):
        """Save the changes made."""
        
        try:
            self.__config.write(open(self.__filename, 'w'))
        except IOError:
            raise exceptions.SidewalkSettingsFileIOError(filename=self.__filename, permission='w')
    

    def add(self, key, activity_processor):
        """Add a new activity processor."""
        
        self.__activity_processor_pairs[key] = activity_processor
        
        for activity_processor_key in self.__activity_processor_pairs.keys():
            self.__config.set('activity_processors', activity_processor_key, self.__activity_processor_pairs[activity_processor_key])
    

    def remove(self, key):
        """Remove the specified activity processor by its key."""
        
        try:
            del self.__activity_processor_pairs[key]
            self.__config.remove_option('activity_processors', key)
        except KeyError:
            raise exceptions.SidewalkKeyDoesNotExist(key=key)


    def remove_group(self, group_key):
        """Remove the specified activity processors by their group key."""
        
        success = False
        for activity_processor_key in self.__activity_processor_pairs.keys():
            if activity_processor_key.find(group_key) == 0:
                self.remove(activity_processor_key)
                success = True
        
        if not success:
            raise exceptions.SidewalkGroupDoesNotExist(group_key=group_key)


    def get_activity_processor(self, key):
        """Get the specified activity processor by its key."""
        
        try:
            return self.__activity_processor_pairs[key]
        except KeyError:
            raise exceptions.SidewalkKeyDoesNotExist(key=key)
 

    def get_activity_processor_pairs(self, key_list=None):
        """Get the specified activity processor pairs. Pairs are returned as a dictionary
        where the key of the dict is the activity processor's key and the dict's associated
        value is the activity processor's path.
        
        If no key list is specified, all of the defiend activity processor pairs are returned.
        """
        
        if key_list == None:
            return self.__activity_processor_pairs
        else:
            pairs = {}
            for key in key_list:
                pairs[key] = self.get_activity_processor(key=key)
                    
            return pairs
  

    def get_group_activity_processor_pairs(self, group_key):
        """Get the specified activity processor pairs with the specified group key."""
        
        pairs = {}
        for activity_processor_key in self.__activity_processor_pairs.keys():
            if activity_processor_key.find(group_key) == 0:
                pairs[activity_processor_key] = self.get_activity_processor(activity_processor_key)
        
        if len(pairs) == 0:
            raise exceptions.SidewalkGroupDoesNotExist(group_key=group_key)
            
        return pairs


__root_dir = os.path.abspath(os.path.dirname(__file__))
def get_conf(path):
    """Get the path of the requested configuration file."""
    
    return os.path.join(__root_dir, 'conf', path)
