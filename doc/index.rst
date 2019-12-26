.. code-block::

                 _____                    _   _
     _ __  _   _| ____|_  _____ ___ _ __ | |_(_) ___  _ __  ___
    | '_ \| | | |  _| \ \/ / __/ _ \ '_ \| __| |/ _ \| '_ \/ __|
    | |_) | |_| | |___ >  < (_|  __/ |_) | |_| | (_) | | | \__ \
    | .__/ \__, |_____/_/\_\___\___| .__/ \__|_|\___/|_| |_|___/
    |_|    |___/                   |_|

pyExceptions Documentation
##########################

An exception base-class to derive more powerful exceptions.

.. admonition:: Exception Hierarchies

   Write how to plan and implement an exception hierarchy.

.. inheritance-diagram:: Exception hierarchy
   :top-classes: pyExceptions.EnvironmentException pyExceptions.PlatformNotSupportedException pyExceptions.NotConfiguredException
   :parts: 1



Exceptions
**********

Base Exception
==============

* :exc:`~pyExceptions.ExceptionBase`

Predefined Exceptions
=====================

* :exc:`~pyExceptions.EnvironmentException`
* :exc:`~pyExceptions.PlatformNotSupportedException`
* :exc:`~pyExceptions.NotConfiguredException`


Contributors
************

* `Patrick Lehmann <https://github.com/Paebbels>`_ (Maintainer)



License
*******

This library is licensed under **Apache License 2.0**.

------------------------------------

.. |docdate| date:: %b %d, %Y - %H:%M

.. only:: html

   This document was generated on |docdate|.

.. toctree::
   :caption: Overview
   :hidden:

   Installation
   Dependencies

.. toctree::
   :caption: Exception Classes
   :hidden:

   ExecptionBase
   Predefined

.. toctree::
   :caption: Appendix
   :hidden:

   License
   genindex

.. #
   py-modindex
