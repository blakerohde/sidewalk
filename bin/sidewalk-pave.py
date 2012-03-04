#!/usr/bin/python

import optparse

from sidewalk.activity_aggregator import ActivityAggregator

def main():
	parser = optparse.OptionParser()
	parser.add_option(
			'-a', '--activity-processor', action='append', default=[],
			dest='activity_processor_keys',
			help='select the activity processor(s) to run by key (format: \'[group.]name\')',
			type='string')
	parser.add_option(
			'-g', '--group', action='append', default=[], 
			dest='group_keys',
			help='select the activity processor group(s) to run by key (format: \'group\')',
			type='string')
	parser.add_option(
			'-v', '--verbose', action='store_true', default=False, 
			dest='verbose',
			help='enable debug messages')
	
	(options, args) = parser.parse_args()
	
	aggregator = ActivityAggregator(
					active_activity_processor_keys=options.activity_processor_keys,
					active_group_keys=options.group_keys,
					verbose=options.verbose)
	aggregator.run()

if __name__ == '__main__':
	main()