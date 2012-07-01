.. _install:

Setup
=====

To setup Sidewalk on your system, please follow the Installation and Run sections below.

Installation 
------------

Install Sidewalk via `pip <http://pypi.python.org/pypi/pip/>`_:

::

        $ pip install sidewalk

If pip is not available on your system, you can also install via easy_install:

::

        $ easy_install sidewalk

If `PyPi <http://pypi.python.org/pypi/sidewalk/>`_ is down or you otherwise cannot use it, you can also install Sidewalk with pip using the GitHub-hosted tarball:

::

        $ pip install -Iv https://github.com/blakerohde/sidewalk/tarball/master

To install without pip or PyPi, download the `source tarball <https://github.com/blakerohde/sidewalk/tarball/master>`_ and run the following in the un-tarred directory:

::

        $ python setup.py install

Run
---

Now that Sidewalk is installed on your system, you can verify both ``sidewalk-conf.py`` and ``sidewalk-pave.py`` are correctly installed by executing the following:

::

        $ sidewalk-conf.py --help

::

        $ sidewalk-pave.py --help


