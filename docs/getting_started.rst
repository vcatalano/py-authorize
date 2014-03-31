Getting Started
===============

The first step when using the Py-Authorize API is to initialize the client 
with your Authorize.net API login name and transaction key. The 
initialization will only need to occur once in your application and must be 
setup before any other API calls are used.

Test Environment
~~~~~~~~~~~~~~~~

.. code-block:: python

    import authorize

    authorize.Configuration.configure(
        authorize.Environment.TEST,
        'api_login_id',
        'api_transaction_key',
    )

In addition to the Authorize.net API login name and transaction key, the 
``configure`` method also takes an ``Environment`` parameter. For development
and testing configurations users should use the ``Environment.TEST'`` 
variable. For production configurations, users should use the 
``Environment.PRODUCTION`` variable:

Production Environment
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    import authorize

    authorize.Configuration.configure(
        authorize.Environment.PRODUCTION,
        'api_login_id',
        'api_transaction_key',
    )

