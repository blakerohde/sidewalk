SHELL := /bin/bash

###
 # Copyright (c) 2012 by Blake Rohde.
 # License: ISC, see LICENSE for more details.
 ##

#TODO: when running tests in Makefile, local dir is in PYTHONPATH, so it will run local copies of this package, and not the site-packages copy
export PYTHONPATH

export VIRTUAL_ENV

# ENV contains the bin/ and lib/ directories where we will install our package
# ENV can be manually set by 'make <target> ENV=/python/install/path'
# If it is not set manually, assign it a value
# WARNING: 'sudo' does NOT preserve VIRTUAL_ENV, so we must pass it in: sudo make <target> ENV=$VIRTUAL_ENV
ifndef ENV
	# If VIRTUAL_ENV is set (typically by a call to a virtualenv's activate), set ENV to VIRTUAL_ENV
	ifneq ($(VIRTUAL_ENV),)
		ENV = $(VIRTUAL_ENV)
	else
		ENV = /usr
	endif
endif

# Use $(BIN) when referencing our bin executables so we don't run the copies in ./bin. Doh!
BIN = $(ENV)/bin/

PYTHON ?= $(BIN)python

all: clean install test

clean:
	@echo -e "\nclean:"
	rm -rf ./MANIFEST
	rm -rf ./dist
	rm -rf ./sidewalk.conf
	rm -rf ./sidewalk_activity_processors/*.pyc
	rm -rf ./sidewalk/*.pyc
	
uninstall:
	@echo -e "\nuninstall:"
	pip uninstall sidewalk

build:
	@echo -e "\nbuild:"
	$(PYTHON) setup.py sdist

install: build
	@echo -e "\ninstall:"
	pip install ./dist/sidewalk-0.2.0.tar.gz

test: sidewalk-conf sidewalk-pave

###
 # Run sidewalk-conf.py tests
 ##
sidewalk-conf: sc-init sc-list sc-add-multiple sc-remove sc-remove-group sc-remove-remaining-tests sc-add-single

sc-init:
	@echo -e "\nsc-init:"
	$(BIN)sidewalk-conf.py ./sidewalk.conf --init
sc-list:
	@echo -e "\nsc-list:"
	$(BIN)sidewalk-conf.py ./sidewalk.conf --list

sc-add-multiple:
	@echo -e "\nsc-add-multiple:"
	$(BIN)sidewalk-conf.py ./sidewalk.conf --add 'tests.import_test sidewalk_activity_processors.example.import_test' --add 'duplicate.import_test_dup_1 sidewalk_activity_processors.example.import_test' --add 'duplicate.import_test_dup_2 sidewalk_activity_processors.example.import_test' --add 'duplicate.import_test_dup_3 sidewalk_activity_processors.example.import_test' --list

sc-remove:
	@echo -e "\nsc-remove:"
	$(BIN)sidewalk-conf.py ./sidewalk.conf --remove 'duplicate.import_test_dup_1' --list

sc-remove-group:
	@echo -e "\nsc-remove-group:"
	$(BIN)sidewalk-conf.py ./sidewalk.conf --remove-group 'duplicate' --list

sc-remove-remaining-tests:
	@echo -e "\nsc-remove-remaining-tests:"
	$(BIN)sidewalk-conf.py ./sidewalk.conf --remove-group 'tests' --list

sc-add-single:
	@echo -e "\nsc-add-single:"
	$(BIN)sidewalk-conf.py ./sidewalk.conf --add 'example.hello sidewalk_activity_processors.example.hello'


###
 # Run sidewalk-pave.py tests (also uses sidewalk-conf.py)
 ##
sidewalk-pave: sc-list sp-valid-activity-processor sp-invalid-activity-processor sp-valid-activity-processor-group sp-invalid-activity-processor-group sp-baddie-activity-processor

sp-valid-activity-processor:
	@echo -e "\nsp-valid-activity-processor:"
	$(BIN)sidewalk-pave.py ./sidewalk.conf --activity-processor 'example.hello'

sp-invalid-activity-processor:
	@echo -e "\nsp-invalid-activity-processor:"
	$(BIN)sidewalk-pave.py ./sidewalk.conf --activity-processor 'example.does_not_exist'

sp-valid-activity-processor-group:
	@echo -e "\nsp-valid-activity-processor-group:"
	$(BIN)sidewalk-pave.py ./sidewalk.conf --group 'example'

sp-invalid-activity-processor-group:
	@echo -e "\nsp-invalid-activity-processor-group:"
	$(BIN)sidewalk-pave.py ./sidewalk.conf --group 'invalid_group'

sp-baddie-activity-processor:
	@echo -e "\nsp-baddie-activity-processor:"
	$(BIN)sidewalk-conf.py ./sidewalk.conf --add 'tests.goodie sidewalk_activity_processors.example.import_test' --add 'tests.baddie_unhandled sidewalk_activity_processors.example.baddie_unhandled_test' --add 'tests.baddie_module foo.bar' --add 'tests.baddie_method sidewalk.foobar' --list
	$(BIN)sidewalk-pave.py ./sidewalk.conf --activity-processor 'tests.baddie_module'
	$(BIN)sidewalk-pave.py ./sidewalk.conf --activity-processor 'tests.baddie_method'
	$(BIN)sidewalk-pave.py ./sidewalk.conf --activity-processor 'tests.baddie_unhandled'
	$(BIN)sidewalk-conf.py ./sidewalk.conf --remove-group 'tests'
