History
-------

0.2.0 (2012-06-30)
++++++++++++++++++

- New Makefile for easier development testing
- Sidewalk is production-ready; bumped version to 0.2.0
- Documentation is now available under ``docs/``
- Specifying a 'custom' settings file is now required; see the documentation for more information on this

0.1.1 (2012-03-08)
++++++++++++++++++

- Moved log functions into new module ``sidewalk.loggers``
- Added exception for when custom settings file's don't have the required section(s)
- ``sidewalk-conf.py --list`` now returns a sorted list

0.1.0 (2012-03-08)
++++++++++++++++++

- Updated README to better represent what it is that Sidewalk actually does
- Added basic log functions and made error messages prettier
- Created ``sidewalk.exceptions`` module and associated exceptions
- Unhandled exceptions thrown by rogue activity processors are now caught
- ``sidewalk-conf.py`` no longer rewrites configuration file if only ``--list`` is requested
- Can now specify filename in ``sidewalk-conf.py`` and ``sidewalk-pave.py`` to use custom Sidewalk settings file/location

0.0.1 (2012-03-04)
++++++++++++++++++

- Initial release
- Wanted initial commit message to read "Pikachu I commit you!" but I flubbed it up and put "Pikachu I choose you!" Oh well.
