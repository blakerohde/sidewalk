Sidewalk: Simple Activity Aggregator
====================================

Sidewalk allows you to trigger the execution of Python methods from the command-line.

Simply register your activity processor (any defined method in any module) and you can execute it using the included command-line utilities: ``sidewalk-conf.py`` and ``sidewalk-pave.py``, respectively.

This comes in handy when you want to setup cron jobs to execute Python code. You can easily create multiple cron job entries that run at various times and call different activity processors.


Documentation and Getting Started
---------------------------------

Formal documentation coming soon. Sorry about that. But don't leave now! Here is a quick run-down of how to get started:

**Step 0) Create an activity processor.**

- This can be any function defined in any module.
- It is recommended that you create a local package to keep all of your activity processors in one location.
- Sidewalk comes with a package ``sidewalk_activity_processors`` for you to use if you would like.
- Note that in this sample package, ``sidewalk_activitiy_processors``, there is an activity processor 'hello' in the module 'example'.

**Step 1) Register your activity processor:**

::

	$ sidewalk-conf.py --add 'example.hello sidewalk_activity_processors.example.hello'

- The sidwalk-conf.py command-line utility is your way to easily add, list/view, and remove activity processors.
- Note that when adding your activity processors, you are creating a key association to the activity processor. Also note the syntax: 'example.hello', in this case, 'example' is the group and 'hello' is the name. Groups are useful for executing multiple activity processors in one go. See step 2 below for more information.

**Step 2) Execute your activity processor:**

::

	$ sidewalk-pave.py --activity-processor 'example.hello'

- Here we are executing our activity processor 'example.hello'.
- You can execute any number of activity processors in one call.
- You can also select activity processors by group.


Installation
------------

To install Sidewalk, download the source by clicking the '`Downloads <https://github.com/blakerohde/sidewalk/downloads>`_' link above, and running the following in the un-zipped/un-tarred directory:

::

	$ python setup.py install


Authors
-------

`Blake Rohde <http://www.blakerohde.com/>`_
