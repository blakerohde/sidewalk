Sidewalk: Simple Activity Aggregator
====================================

Sidewalk allows you to run your Python code from the command-line.

This comes in handy when you want to setup cron jobs to execute Python code.

Simply register your activity processor (any defined method in any module) and you can execute it using the included command-line utilities: 'sidewalk-conf.py' and 'sidewalk-pave.py', respectively.


Documentation and Demos
-----------------------

Formal documentation coming soon. Sorry about that. But don't leave now! Here is a quick run-down of how to get started:

**0) Create an activity processor.**

- This can be any function defined in any module.
- It is recommended that you create a local package to keep all of your activity processors in one location.
- Sidewalk comes with a package 'sidewalk_activity_processors' for you to use if you would like.
- Note that in this sample package, 'sidewalk_activitiy_processors', there is an activity processor 'hello' in the module 'example'

**1) Register your activity processor:**

::

	>>> sidewalk-conf.py --add 'example.hello sidewalk_activity_processors.example.hello'

- The sidwalk-conf.py command-line utility is your way to easily add, list, and remove activity processors.
- Note that when adding your activity processors, you are creating a key association to the activity processor. Also note the syntax: 'example.hello', in this case, 'example' is the group and 'hello' is the name. Groups are useful for executing multiple activity processors in one go. See step 2 below for more information.

**2) Execute your activity processor:**

::

	>>> sidewalk-pave.py --activity-processor 'example.hello'

- Here we are executing our activity processor 'example.hello'.
- You can execute any number of activity processors in one call.
- You can also select activity processors by group.


Authors
-------

`Blake Rohde <http://www.blakerohde.com/>`_