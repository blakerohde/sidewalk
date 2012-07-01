#!/usr/bin/python

import argparse
import traceback

import sidewalk.loggers
import sidewalk.manager
import sidewalk.exceptions
from sidewalk.activity_aggregator import ActivityAggregator

def main():
	parser = argparse.ArgumentParser()
	
	parser.add_argument('filename', default='',
			help='settings file used to store Sidewalk settings and configuration')
	parser.add_argument('-a', '--activity-processor', dest='activity_processor_keys', action='append', default=[],
			help='select the activity processor(s) to run by key (format: \'[group.]name\')')
	parser.add_argument('-g', '--group', dest='group_keys', action='append', default=[],
			help='select the activity processor group(s) to run by key (format: \'group\')')
	parser.add_argument('-v', '--verbose', action='store_true', default=False,
			help='enable debug messages')
	
	args = parser.parse_args()
	
	try:
		aggregator = ActivityAggregator(filename=args.filename, active_activity_processor_keys=args.activity_processor_keys,
						active_group_keys=args.group_keys, verbose=args.verbose)
		
		aggregator.run()
	except sidewalk.exceptions.SidewalkSettingsFileIOError, e:
		sidewalk.loggers.error('Settings file IOError for requested file "%s"' % (
			e.filename
		))
	except sidewalk.exceptions.SidewalkSectionNotDefined, e:
		sidewalk.loggers.error('Settings file "%s" does not have the required section "%s"' % (
			e.filename,
			e.section
		))
	except sidewalk.exceptions.SidewalkKeyDoesNotExist, e:
		sidewalk.loggers.error('Invalid key "%s"' % (
			e.key
		))
	except sidewalk.exceptions.SidewalkGroupDoesNotExist, e:
		sidewalk.loggers.error('Invalid group key "%s"' % (
			e.group_key
		))
	except sidewalk.exceptions.SidewalkModuleImportError, e:
		sidewalk.loggers.error('Cannot import module "%s" OR a module used/called WITHIN module "%s"' % (
			e.module,
			e.module
		))
	except sidewalk.exceptions.SidewalkMethodDoesNotExist, e:
		sidewalk.loggers.error('Method "%s" not defined in module "%s"' % (
			e.method,
			e.module
		))
	except sidewalk.exceptions.SidewalkRogueActivityProcessor, e:
		sidewalk.loggers.error('Activity processor "%s" threw an unhandled exception' % (
			e.activity_processor
		))
		
if __name__ == '__main__':
	main()
