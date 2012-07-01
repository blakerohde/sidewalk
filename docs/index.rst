.. Sidewalk documentation master file, created by
   sphinx-quickstart on Sun May  6 18:48:59 2012.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Sidewalk: Simple Activity Aggregator
====================================

Sidewalk allows you to trigger the execution of Python methods from the command-line.

Simply register your activity processor (any defined method in any module) and you can execute it using the included command-line utilities ``sidewalk-conf.py`` and ``sidewalk-pave.py``, respectively.

This comes in handy when you want to setup cron jobs to execute Python code. You can easily create multiple cron job entries that run at various times and call different activity processors.


User Guide
----------

This section of the documentation provides the user of Sidewalk a guide for how to use the two interfaces: ``sidewalk-conf.py`` and ``sidewalk-pave.py``.

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

   sidewalk


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

