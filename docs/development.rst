Development
===========

Any development help is greatly appreciated. If you have have any new 
features, bug fixes or documentation improvements please feel free to 
contribute.


Getting started
---------------

To start developing on this project, fork this project on our `Github page`_
and install from source using the instructions in :doc:`Install <install>`. 
Additionally, you will need to install the following dependencies for running
test and compiling documentation.

- nose_
- sphinx_ (for documentation)

.. _Github page: https://github.com/vcatalano/py-authorize
.. _nose: https://nose.readthedocs.org/en/latest/
.. _sphinx: http://sphinx-doc.org/


Running Tests
-------------

This project has been configured to use the Nose testing framework. 
The following command will run all tests for the project. Since many of the 
tests connect to the Authorize.net server, running the tests may take quite a 
few seconds.

.. code-block:: bash

    nosetests

To run only local tests, you can use the following command:

.. code-block:: bash

    nosetests -a '!live_tests'


Authorize.net documentation
---------------------------

The Authorize.net documentation can be overly verbose and very inconsistent 
with the implementations of many of its features. You can view the 
documentation by visiting the following links:

- `Developer site`_
- `Advanced Integration Method`_
- `Customer Information Manager`_
- `Automated Recurring Billing`_

.. _Developer site: http://developer.authorize.net/
.. _Advanced Integration Method: http://www.authorize.net/support/AIM_guide_XML.pdf
.. _Customer Information Manager: http://www.authorize.net/support/CIM_XML_guide.pdf
.. _Automated Recurring Billing: http://www.authorize.net/support/ARB_guide.pdf


Submitting bugs and patches
---------------------------

All bug reports, new feature requests and pull requests are handled through 
this project's `Github issues`_ page.

.. _Github issues: https://github.com/vcatalano/py-authorize/issues
