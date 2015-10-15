Python Recode
=============

This python extension contains a simple binding to the GNU Recode library.
This module requires GNU Recode 3.5 and its development headers.


Compilation
-----------

Run the following command:

    python setup.py build


For additional options:

    python setup.py build --help


Installation
------------

    python setup.py install

For additional options:

    python setup.py install --help


Troubleshooting
---------------

Here are listed some common problems while building the python-recode
module.

GNU Recode is not in a standard place
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To build, run:

    python setup.py build_ext -I /path/to/recode/include -L /path/to/recode/lib


The installation fails with one of the following errors:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

*"the recode module is broken."*

This means that you are using an inadequate version of GNU Recode. You
need to use either Recode 3.5, or Recode 3.6 with some extra patches.
**The stock version of Recode 3.6 from any GNU mirror DOES NOT WORK.**

*"the recode library is probably broken."*

This means that GNU Recode has been compiled with a buggy version of
gcc (gcc-3.3.2 seems to trigger this problem). You can recompile
recode with the following option for configure:

    CFLAGS=-g ./configure --prefix=...
