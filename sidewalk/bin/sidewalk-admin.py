#!/usr/bin/env python

import sys
import argparse
import os.path
import traceback

from sidewalk.core import exceptions, loggers
from sidewalk.core.manager import ActivityProcessorsManager
from sidewalk.core.activity_aggregator import ActivityAggregator


commands = {
    'init' : {
        'help' : 'if the specified settigns file does not exist, create and initialize it',
    },
    'list' : {
        'help' : 'list the defined activity processors',
    },
    'add' : {
        'help' : 'add an activity processor pair',
        'arguments' : [
            {'key' : {
                'help' : 'activity processor pair key; format: [group.[subgroup.[...]]]name',
            }},
            {'callable' : {
                'help' : 'callable for activity processor; typical format: [package.module.]function',
            }},
        ],
    },
    'remove' : {
        'help' : 'remove an activity processor by key',
        'arguments' : [
            {'key' : {
                'help' : 'activity processor pair key; format: [group.[subgroup.[...]]]name',
            }},
        ],
    },
    'remove-group' : {
        'help' : 'remove an activity processor group by key',
        'arguments' : [
            {'key' : {
                'help' : 'group key; format: goup',
            }},
        ],
    },
    'pave' : {
        'help' : 'select the activity processor(s) to run by key',
        'arguments' : [
            {'key' : {
                'nargs' : '?',
                'help' : 'activity processor pair key; format: [group.[subgroup.[...]]]name',
            }},
        ],
    },
}


def main(argv):
    parser = argparse.ArgumentParser()
    
    parser.add_argument('filename', default='',
            help='settings file used to store Sidewalk settings and configuration')
    parser.add_argument('command', default='', choices=commands.keys(),
            help='command to run')
    parser.add_argument('-v', '--verbose', action='store_true', default=False,
            help='enable debug messages')
    
    # If more than 1 argument, assume there are more required positioanl arguments and register them
    if len(argv) > 1 and argv[1] in commands:
        for argument in commands[argv[1]].get('arguments', []):
            arg_name = argument.keys()[0]
            tmp = parser.add_argument(arg_name, default=argument[arg_name].get('default', ''),
                    help=argument[arg_name].get('help', ''))
            
            if 'nargs' in argument[arg_name]:
                tmp.nargs = argument[arg_name]['nargs']
    
    args = parser.parse_args(args=argv)
    
    try:
        # Create and inilize the settings file if it doesn't exist
        if args.command == 'init' and not os.path.exists(args.filename):
            settings_file = open(args.filename, 'w')
            settings_file.write('[activity_processors]')
            settings_file.close()
        # Pave/run the specified activity processors
        elif args.command == 'pave':
            print args.key
            aggregator = ActivityAggregator(filename=args.filename, active_activity_processor_keys=[args.key], verbose=args.verbose)
            
            aggregator.run()
        # Else, use the manager to edit the existing settings file
        else:
            manager = ActivityProcessorsManager(filename=args.filename)
            
            if args.command == 'remove':
                manager.remove(args.key)
                manager.save()
            elif args.command == 'remove-group':
                manager.remove_group(args.key)
                manager.save()
            elif args.command == 'add':
                manager.add(args.key, args.callable)
                manager.save()
            elif args.command == 'list':
                for activity_processor_key in sorted(manager.get_activity_processor_pairs().keys()):
                    print '%s : %s' % (activity_processor_key, manager.get_activity_processor(activity_processor_key))
    except exceptions.SidewalkSettingsFileIOError, e:
        loggers.error('Could not open settings file "%s" with "%s" permissions.' % (
            e.filename,
            e.permission,
        ))
        sys.exit(1)
    except exceptions.SidewalkSectionNotDefined, e:
        loggers.error('Settings file "%s" does not have the required section "%s". Try running ``init`` command.' % (
            e.filename,
            e.section,
        ))
        sys.exit(1)
    except exceptions.SidewalkKeyDoesNotExist, e:
        loggers.error('Invalid key "%s".' % (
            e.key,
        ))
        sys.exit(1)
    except exceptions.SidewalkGroupDoesNotExist, e:
        loggers.error('Invalid group key "%s".' % (
            e.group_key,
        ))
        sys.exit(1)
    except exceptions.SidewalkMethodDoesNotExist, e:
        loggers.error('Activity processor "%s" in module "%s" could not be executed. This is most likely caused by a compile-time exception. Try running again with the ``--verbose`` flag.' % (
            e.method,
            e.module,
        ))
        sys.exit(1)
    except:
        loggers.error('Unexpected exception: \n%s\nThis is most likely caused by a runtime exception. Try running again with the ``--verbose`` flag.' % (
            traceback.format_exc(),
        ))
        sys.exit(1)
    
    sys.exit()


if __name__ == '__main__':
    main(sys.argv[1:])
