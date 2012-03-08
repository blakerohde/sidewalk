#!/usr/bin/python

import optparse
import traceback

import sidewalk
import sidewalk.manager
import sidewalk.exceptions
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
			'-f', '--settings-file', action='store', default=None,
			dest='filename',
			help='settings file used to store Sidewalk settings and configuration',
			type='string')
	parser.add_option(
			'-v', '--verbose', action='store_true', default=False, 
			dest='verbose',
			help='enable debug messages')
	
	(options, args) = parser.parse_args()
	
	try:
		filename = ''
		if options.filename == None:
			filename = sidewalk.manager.get_conf('settings.conf')
		else:
			filename = options.filename
		
		aggregator = ActivityAggregator(
						filename=filename,
						active_activity_processor_keys=options.activity_processor_keys,
						active_group_keys=options.group_keys,
						verbose=options.verbose)
		
		aggregator.run()
	except sidewalk.exceptions.SidewalkSettingsFileIOError, e:
		sidewalk.error_log('Settings file IOError for requested file "%s"' % (
			e.filename
		))
	except sidewalk.exceptions.SidewalkKeyDoesNotExist, e:
		sidewalk.error_log('Invalid key "%s"' % (
			e.key
		))
	except sidewalk.exceptions.SidewalkGroupDoesNotExist, e:
		sidewalk.error_log('Invalid group key "%s"' % (
			e.group_key
		))
	except sidewalk.exceptions.SidewalkModuleImportError, e:
		sidewalk.error_log('Cannot import module "%s"' % (
			e.module
		))
	except sidewalk.exceptions.SidewalkMethodDoesNotExist, e:
		sidewalk.error_log('Method "%s" not defined in module "%s"' % (
			e.method,
			e.module
		))
	except sidewalk.exceptions.SidewalkRogueActivityProcessor, e:
		sidewalk.error_log('Activity processor "%s" threw an unhandled exception' % (
			e.activity_processor
		))
		
if __name__ == '__main__':
	main()