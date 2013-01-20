.. Sidewalk documentation master file, created by
   sphinx-quickstart on Sun May  6 18:48:59 2013.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Sidewalk: Simple Activity Aggregator
====================================

Sidewalk allows you to easily trigger the execution of sets of Python methods from the command-line.

Simply register your activity processors (i.e. functions/methods) with key associations and execute them by key or group using the included command-line utility ``sidewalk``.

This comes in handy when you want to setup cron jobs to execute Python code. You can easily create multiple cron job entries that run at various times and call different sets of activity processors.


User Guide
----------

This section of the documentation provides the user of Sidewalk a guide for how to use the command-line interface through the ``sidewalk`` executable.

.. toctree::
   :maxdepth: 3

   user/intro
   user/install
   user/use


API Documentation
-----------------

This section provides a technical overview of the underlying logic that drives Sidewalk.

.. toctree::
   :maxdepth: 2

   api/sidewalk


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

