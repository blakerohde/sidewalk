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
	long_description=open('README.rst').read() + '\n\n' +
                     open('HISTORY.rst').read(),
	download_url='https://github.com/blakerohde/sidewalk/tarball/master',
	scripts=[
		'sidewalk/bin/sidewalk',
	],
	packages=[
		'sidewalk',
        'sidewalk.bin',
        'sidewalk.conf',
        'sidewalk.core',
        'sidewalk.test',
	],
	package_data={
		'' : [
            'LICENSE',
		],
	},
	license=open('LICENSE').read(),
	classifiers=(
		'Development Status :: 5 - Production/Stable',
		'Environment :: Console',
		'Topic :: System :: Logging',
		'Topic :: System :: Monitoring',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: ISC License (ISCL)',
		'Natural Language :: English',
		'Programming Language :: Python',
		'Programming Language :: Python :: 2.6',
		'Programming Language :: Python :: 2.7',
	),
)
