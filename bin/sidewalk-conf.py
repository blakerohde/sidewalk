#!/usr/bin/python

import optparse

import sidewalk
from sidewalk.manager import ActivityProcessorsManager

def main():
	parser = optparse.OptionParser()
	parser.add_option(
			'-l', '--list', action='store_true', default=False,
			dest='list',
			help='list the defined activity processors')
	parser.add_option(
			'-a', '--add', action='append', default=[],
			dest='new_activity_processor_pairs',
			help='add an activity processor pair (format: \'[group.]name = package.module.function\')',
			type='string')
	parser.add_option(
			'--remove', action='append', default=[],
			dest='remove_activity_processor_keys',
			help='remove an activity processor by key (format: \'[group.]name\')',
			type='string')
	parser.add_option(
			'--remove-group', action='append', default=[],
			dest='remove_activity_processor_group_keys',
			help='remove an activity processor group by key (format: \'group\')',
			type='string')
	parser.add_option(
			'-v', '--verbose', action='store_true', default=False, 
			dest='verbose',
			help='enable debug messages')
	
	(options, args) = parser.parse_args()
	
	manager = ActivityProcessorsManager(sidewalk.get_conf('settings.conf'))
	
	# Remove requested activity processors
	for activity_processor_key in options.remove_activity_processor_keys:
		manager.remove(activity_processor_key)
	
	# Remove requested activity processor groups
	for group_key in options.remove_activity_processor_group_keys:
		manager.remove_group(group_key)
	
	# Add requested activity processors
	for activity_processor_pair in options.new_activity_processor_pairs:
		(key, activity_processor) = activity_processor_pair.split(' ', 1)
		manager.add(key, activity_processor)
	
	# List defined activity_processors, if requestd
	if options.list:
		for activity_processor_key in manager.get_activity_processor_pairs().keys():
			print '%s: %s' % (activity_processor_key, manager.get_activity_processor(activity_processor_key))
	
	# Write changes made
	manager.save()
	
if __name__ == '__main__':
	main()