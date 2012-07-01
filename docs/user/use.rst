.. _use:

How to use Sidewalk
===================

This section of the documentation provides commentary for how to use Sidewalk.

This page of documentation will be expanded in the furture. In the mean time, here is a quick run-down for how to get started:

Create Activity Processors
--------------------------

- This can be any function defined in any module.
- It is recommended that you create a local package to keep all of your activity processors in one location.
- Sidewalk comes with a package ``sidewalk_activity_processors`` for you to use if you would like.
- Note that in this sample package, ``sidewalk_activitiy_processors``, there is an activity processor 'hello' in the module 'example'.

Create A Settings File
----------------------

Before we can register our activity processors, we need to create and initialize a settings file. This file will contain a list of registered activity processors. It is up to you where to put the settings file. You can create a single settings file for an entire system, or create one for each of your projects. For right now, lets just create one in the current working directory:

::

        $ sidewalk-conf.py ./sidewalk.conf --init

Register Activity Processors
----------------------------

::

        $ sidewalk-conf.py ./sidewalk.conf --add 'example.hello sidewalk_activity_processors.example.hello'

- The sidwalk-conf.py command-line utility is your way to easily add, list/view, and remove activity processors.
- Note that when adding your activity processors, you are creating a key association to the activity processor. Also note the syntax: 'example.hello', in this case, 'example' is the group and 'hello' is the name. Groups are useful for executing multiple activity processors in one go. See step 2 below for more information.

Execute Activity Processors
---------------------------

::

        $ sidewalk-pave.py ./sidewalk.conf --activity-processor 'example.hello'

- Here we are executing our activity processor 'example.hello'.
- You can execute any number of activity processors in one call.
- You can also select activity processors by group.

