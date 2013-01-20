Sidewalk: Simple Activity Aggregator
====================================

Sidewalk allows you to easily trigger the execution of sets of Python methods from the command-line.

Simply register your activity processors (i.e. functions/methods) with key associations and execute them by key or group using the included command-line utility ``sidewalk``.

This comes in handy when you want to setup cron jobs to execute Python code. You can easily create multiple cron job entries that run at various times and call different sets of activity processors.


Documentation and Getting Started
---------------------------------

Formal documentation is available on `Read the Docs <http://sidewalk.readthedocs.org/en/latest/>`_ and is also located in the ``docs/`` directory of the source code.

Here is a quick run-down for how to get started:

**Step 0) Create an activity processor.**

- This can be any function defined in any module.
- It is common to create an ``activitiy_processors/`` directory in your project's main directory to hold all of the activity processors specific to that project. This directory is also typically used to the project's Sidewalk configuration file (see Step 1 below).
- Note Sidewalk comes with an example activitiy processor ``hello`` in the module ``sidewalk.test.example``.

**Step 1) Create a configuration file:**

Before we can register our activity processors, we need to create and initialize a configurationfile. This file will contain a list of registered activity processors. It is up to you where to put the configuration file. You can create a single configuration file for an entire system, or create one for each of your projects. For right now, lets just create one in the current working directory:

::

        $ sidewalk ./sidewalk.conf init

**Step 2) Register your activity processor:**

::

	$ sidewalk ./sidewalk.conf add example.hello sidewalk.test.example.hello

- The ``sidewalk`` command-line utility is your way to easily add, list/view, and remove activity processors.
- Note that when adding your activity processors, you are creating a key association to the activity processor. Also note the syntax: ``example.hello``, in this case, ``example`` is the group and ``hello`` is the name. Groups are useful for executing multiple activity processors in one go. See step 3 below for more information.

**Step 3) Execute your activity processor:**

::

	$ sidewalk ./sidewalk.conf pave example.hello

- Here we are executing our activity processor ``example.hello``.
- You can select activity processors by group, e.g.: ``$ sidewalk ./sidewalk.conf pave example.``.
- You can execute any number of activity processors in one call, e.g.: ``$ sidewalk ./sidewalk.conf pave example.`` to execute all activity processors of group ``example`` or ``$ sidewalk ./sidewalk.conf pave 
example.hello second_group.`` to execute ``example.hello`` and all activity processors of group ``second_group``.


Installation
------------

Install Sidewalk via `pip <http://pypi.python.org/pypi/pip/>`_:

::

	$ pip install sidewalk

If needed, other methods of installing Sidewalk are noted in the `documentation <http://readthedocs.org/projects/sidewalk/>`_.


Links
-----

- `Sidewalk on PyPI <http://pypi.python.org/pypi/sidewalk>`_
- `Sidewalk on GitHub <https://github.com/blakerohde/sidewalk>`_
- `Issue Tracker <https://github.com/blakerohde/sidewalk/issues>`_

Authors
-------

`Blake Rohde <http://www.blakerohde.com/>`_
