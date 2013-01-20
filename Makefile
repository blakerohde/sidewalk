SHELL := /bin/bash

###
 # Copyright (c) 2013 by Blake Rohde.
 # License: ISC, see LICENSE for more details.
 ##

#TODO: when running tests in Makefile, local dir is in PYTHONPATH, so it will run local copies of this package, and not the site-packages copy
export PYTHONPATH

export VIRTUAL_ENV

BIN ?= ./sidewalk/bin/
PYTHON ?= python

all: clean gen-docs install test
	@echo -e "\nDONE"

pypi-upload:
	@echo -e "\npypi-upload:"
	$(PYTHON) setup.py sdist upload

view-docs:
	@echo -e "\nview-docs:"
	firefox ./docs/_build/html/index.html

gen-docs:
	@echo -e "\ngen-docs:"
	rm ./docs/api/*
	sphinx-apidoc -o ./docs/api ./sidewalk/
	cd ./docs/ && make html

clean:
	@echo -e "\nclean:"
	rm -rf ./MANIFEST
	rm -rf ./dist
	rm -rf ./build
	rm -rf ./sidewalk.conf
	rm -rf `find . -type f -name *.pyc`
	
uninstall:
	@echo -e "\nuninstall:"
	pip uninstall sidewalk

build:
	@echo -e "\nbuild:"
	$(PYTHON) setup.py sdist

install: build
	@echo -e "\ninstall:"
	pip install ./dist/sidewalk-*.tar.gz

test: sidewalk

###
 # Run sidewalk tests
 ##
sidewalk: s-init s-add s-list s-remove 

s-init:
	@echo -e "\ns-init:"
	$(BIN)sidewalk ./sidewalk.conf init

s-list:
	@echo -e "\ns-list:"
	$(BIN)sidewalk ./sidewalk.conf list

s-add:
	@echo -e "\ns-add:"
	$(BIN)sidewalk ./sidewalk.conf add example.hello sidewalk.test.example.hello
	$(BIN)sidewalk ./sidewalk.conf add example.test sidewalk.test.example.import_test
	$(BIN)sidewalk ./sidewalk.conf add example.baddie sidewalk.test.example.baddie_unhandled_test

s-pave:
	@echo -e "\ns-pave:"
	$(BIN)sidewalk ./sidewalk.conf pave example.hello example.import_test

s-remove:
	@echo -e "\ns-remove:"
	$(BIN)sidewalk ./sidewalk.conf remove example.baddie example.
