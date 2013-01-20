.. _use:

How to use Sidewalk
===================

This section of the documentation provides commentary for how to use Sidewalk.

This page of documentation will be expanded in the future. In the mean time, here is a quick run-down for how to get started:

Create Activity Processors
--------------------------

- This can be any function defined in any module.
- It is common to create an ``activitiy_processors/`` directory in your project's main directory to hold all of the activity processors specific to that project. This directory is also typically used to the project's Sidewalk configuration file (see Step 1 below).
- Note Sidewalk comes with an example activitiy processor ``hello`` in the module ``sidewalk.test.example``.

Create A Configuration File
---------------------------

Before we can register our activity processors, we need to create and initialize a configurationfile. This file will contain a list of registered activity processors. It is up to you where to put the configuration file. You can create a single configuration file for an entire system, or create one for each of your projects. For right now, lets just create one in the current working directory:

::

        $ sidewalk ./sidewalk.conf init

Register Activity Processors
----------------------------

::

        $ sidewalk ./sidewalk.conf add example.hello sidewalk.test.example.hello

- The ``sidewalk`` command-line utility is your way to easily add, list/view, and remove activity processors.
- Note that when adding your activity processors, you are creating a key association to the activity processor. Also note the syntax: ``example.hello``, in this case, ``example`` is the group and ``hello`` is the name. Groups are useful for executing multiple activity processors in one go. See step 3 below for more information.

Execute Activity Processors
---------------------------

::

        $ sidewalk ./sidewalk.conf pave example.hello

- Here we are executing our activity processor ``example.hello``.
- You can select activity processors by group, e.g.: ``$ sidewalk ./sidewalk.conf pave example.``.
- You can execute any number of activity processors in one call, e.g.: ``$ sidewalk ./sidewalk.conf pave example.`` to execute all activity processors of group ``example`` or ``$ sidewalk ./sidewalk.conf pave example.hello second_group.`` to execute ``example.hello`` and all activity processors of group ``second_group``.
