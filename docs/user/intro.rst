.. _introduction:

Introduction
============

Why Sidewalk?
-------------

Sidewalk allows you to trigger the execution of Python methods from the command-line.

As the saying goes, there are many ways to skin a cat. Obviously people have been executing python code one way or another via command-line through methods of "python -c", or pointing directly to a Python file and using the "'__name__' == '__main__'" convention, etc.

When you register an activity processor, you assign it a key. You can create group associations when assigning keys (e.g. 'group.sub-group.activity_processor'). You can then execute all of the registered activity processors in one call by referencing the assigned 'group' or 'group.sub-group'. This is a nice feature as it allows you to execute many activity processors, that are potentially located in any number of modules, in one call.

You can also execute any number of groups, and/or any number of specific activity processors, when calling the command-line utility ``sidewalk``. This is a key feature of Sidewalk, as you can easily create multiple cron job entries that run at various times, but call different activity processors. If you wanted to implement similar functionality in a traditional sense, you would have to create multiple modules that reference said activity processors, or create one module and have an if-else statement to do the same.

Sidewalk's License
------------------

    Copyright (c) 2013, Blake Rohde

    Permission to use, copy, modify, and/or distribute this software for any purpose with or without fee is hereby granted, provided that the above copyright notice and this permission notice appear in all copies.

    THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
