Installation
============

Install with pip
----------------

If you are using pip_, you can install the :app:'Py-Authorize' package using the
following commands:

.. code-block:: text

    pip install py-authorize

.. _pip: http://www.pip-installer.org/


Install with virtualenv
-----------------------

If you are using virtualenv_ to manage your packages, you can install 
:app:'Py-Authorize' using the following commands:

.. code-block:: text

    easy_install py-authorize

.. _virtualenv: http://www.virtualenv.org/


Install from source
-------------------

Download or clone the source from Github and run setup.py install:

.. code-block:: text

    git clone http://github.com/vcatalano/py-authorize.git
    cd py-authorize
    python setup.py install


Requirements
------------

Py-Authorize has only one external dependency:

* colander_

If you want to build the docs or run the tests, there are additional
dependencies, which are covered in the :doc:`development` section.

.. _colander: http://docs.pylonsproject.org/projects/colander