#!/usr/bin/python

import argparse
import os.path

import sidewalk.loggers
import sidewalk.manager
from sidewalk.manager import ActivityProcessorsManager

def main():
	parser = argparse.ArgumentParser()
	
	parser.add_argument('filename', default='',
			help='settings file used to store Sidewalk settings and configuration')
	parser.add_argument('-i', '--init', action='store_true', default=False,
			help='if the specified settigns file does not exist, create and initialize it')
	parser.add_argument('-l', '--list', action='store_true', default=False,
			help='list the defined activity processors')
	parser.add_argument('-a', '--add', dest='new_activity_processor_pairs', action='append', default=[],
			help='add an activity processor pair (format: \'[group.]name = package.module.function\')')
	parser.add_argument('--remove', dest='remove_activity_processor_keys', action='append', default=[],
			help='remove an activity processor by key (format: \'[group.]name\')')
	parser.add_argument('--remove-group', dest='remove_activity_processor_group_keys', action='append', default=[],
			help='remove an activity processor group by key (format: \'group\')')
	parser.add_argument('-v', '--verbose', action='store_true', default=False,
			help='enable debug messages')
	
	args = parser.parse_args()
	
	try:
		# Create and inilize the settings file if it doesn't exist
		if args.init and not os.path.exists(args.filename):
			settings_file = open(args.filename, 'w')
			settings_file.write('[activity_processors]')
			settings_file.close()
		
		manager = ActivityProcessorsManager(filename=args.filename)
		
		# If we are going to add/remove activity processors
		if (len(args.remove_activity_processor_keys) + len(args.remove_activity_processor_group_keys) + len(args.new_activity_processor_pairs)) > 0:
			# Remove requested activity processors
			for activity_processor_key in args.remove_activity_processor_keys:
				manager.remove(activity_processor_key)
			
			# Remove requested activity processor groups
			for group_key in args.remove_activity_processor_group_keys:
				manager.remove_group(group_key)
			
			# Add requested activity processors
			for activity_processor_pair in args.new_activity_processor_pairs:
				(key, activity_processor) = activity_processor_pair.split(' ', 1)
				manager.add(key, activity_processor)
			
			# Write changes made
			manager.save()
		
		# List defined activity_processors, if requestd
		if args.list:
			for activity_processor_key in sorted(manager.get_activity_processor_pairs().keys()):
				print '%s : %s' % (activity_processor_key, manager.get_activity_processor(activity_processor_key))
	except sidewalk.exceptions.SidewalkSettingsFileIOError, e:
		sidewalk.loggers.error('Could not open settings file "%s" with permission "%s"' % (
			e.filename,
			e.permission
		))
	except sidewalk.exceptions.SidewalkSectionNotDefined, e:
		sidewalk.loggers.error('Settings file "%s" does not have the required section "%s"' % (
			e.filename,
			e.section
		))
		
if __name__ == '__main__':
	main()
