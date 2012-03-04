import os

from distutils.core import setup
import sidewalk

setup(
	name='sidewalk',
	version=sidewalk.__version__,
	url= 'http://www.blakerohde.com/projects/sidewalk',
	author='Blake Rohde',
	author_email='blake@blakerohde.com',
	description='The Simple Activity Aggregator.',
	long_description=open('README.rst').read(),
	download_url='https://github.com/blakerohde/sidewalk/tarball/master',
	scripts=[
		'bin/sidewalk-conf.py',
		'bin/sidewalk-pave.py',
	],
	packages=[
		'sidewalk',
	],
	package_data={
		'' : [
			'LICENSE'
		],
		'sidewalk' : [
			'conf/*.conf'
		],
	},
	license='ISC',
	classifiers=(
		'Development Status :: 2 - Pre-Alpha',
		'Environment :: Console',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: ISC License (ISCL)',
		'Natural Language :: English',
		'Programming Language :: Python',
		'Programming Language :: Python :: 2.6',
		'Programming Language :: Python :: 2.7',
	),
)