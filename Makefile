SHELL := /bin/bash

#TODO: when running tests in Makefile, local dir is in PYTHONPATH, so it will run local copies  of the Sidewalk package, and not the site-packages copy
export PYTHONPATH

# Use $(BIN) when referencing our bin executables so we don't run the copies in ./bin. Doh!
BIN = /usr/bin/

PYTHON ?= python

###
 # all
 #
 # dev-cleanup
 # dev-reinstall
 # dev-install
 # dev-uninstall
 #
 # sidewalk-conf
 # ...
 # sidewalk-pave
 # ...
 ##

###
 # Run all tests
 ##
all: sidewalk-conf sidewalk-pave


###
 # Cleanup the dirs
 ##
dev-cleanup:
	@echo -e "\ndev-cleanup:"
	rm -rf ./build
	rm -rf ./sidewalk/*.pyc
	rm -rf ./sidewalk_activity_processors/*.pyc


###
 # Install the package
 ##
dev-install:
	@echo -e "\ndev-install:"
	$(PYTHON) setup.py install


###
 # Uninstall the package
 ##
dev-uninstall:
	@echo -e "\ndev-uninstall:"
	rm -rf /usr/bin/sidewalk-conf.py
	rm -rf /usr/bin/sidewalk-pave.py
	rm -rf /usr/lib/python2.6/site-packages/sidewalk*


###
 # Reinstall the package (uninstall, cleanup, install)
 ##
dev-reinstall: dev-uninstall dev-cleanup dev-install


###
 # Run sidewalk-conf.py tests
 ##
sidewalk-conf: sc-list sc-add-multiple sc-remove sc-remove-group sc-remove-remaining-tests

sc-list:
	@echo -e "\nsc-list:"
	$(BIN)sidewalk-conf.py --list

sc-add-multiple:
	@echo -e "\nsc-add-multiple:"
	$(BIN)sidewalk-conf.py --add 'tests.import_test sidewalk_activity_processors.example.import_test' --add 'duplicate.import_test_dup_1 sidewalk_activity_processors.example.import_test' --add 'duplicate.import_test_dup_2 sidewalk_activity_processors.example.import_test' --add 'duplicate.import_test_dup_3 sidewalk_activity_processors.example.import_test' --list

sc-remove:
	@echo -e "\nsc-remove:"
	$(BIN)sidewalk-conf.py --remove 'duplicate.import_test_dup_1' --list

sc-remove-group:
	@echo -e "\nsc-remove-group:"
	$(BIN)sidewalk-conf.py --remove-group 'duplicate' --list

sc-remove-remaining-tests:
	@echo -e "\nsc-remove-remaining-tests:"
	$(BIN)sidewalk-conf.py --remove-group 'tests' --list


###
 # Run sidewalk-pave.py tests (also uses sidewalk-conf.py)
 ##
sidewalk-pave: sc-list sp-valid-activity-processor sp-invalid-activity-processor sp-valid-activity-processor-group sp-invalid-activity-processor-group sp-baddie-activity-processor

sp-valid-activity-processor:
	@echo -e "\nsp-valid-activity-processor:"
	$(BIN)sidewalk-pave.py --activity-processor 'example.hello'

sp-invalid-activity-processor:
	@echo -e "\nsp-invalid-activity-processor:"
	$(BIN)sidewalk-pave.py --activity-processor 'example.does_not_exist'

sp-valid-activity-processor-group:
	@echo -e "\nsp-valid-activity-processor-group:"
	$(BIN)sidewalk-pave.py --group 'example'

sp-invalid-activity-processor-group:
	@echo -e "\nsp-invalid-activity-processor-group:"
	$(BIN)sidewalk-pave.py --group 'invalid_group'

sp-baddie-activity-processor:
	@echo -e "\nsp-baddie-activity-processor:"
	$(BIN)sidewalk-conf.py --add 'tests.goodie sidewalk_activity_processors.example.import_test' --add 'tests.baddie_unhandled sidewalk_activity_processors.example.baddie_unhandled_test' --add 'tests.baddie_module foo.bar' --add 'tests.baddie_method sidewalk.foobar' --list
	$(BIN)sidewalk-pave.py --activity-processor 'tests.baddie_module'
	$(BIN)sidewalk-pave.py --activity-processor 'tests.baddie_method'
	$(BIN)sidewalk-pave.py --activity-processor 'tests.baddie_unhandled'
	$(BIN)sidewalk-conf.py --remove-group 'tests'

