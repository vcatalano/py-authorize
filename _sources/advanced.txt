Advanced
========

Out-of-the-box Py-Authorize provides some very basic and powerful 
functionality. For some users and applications, more advanced API 
functionality may be needed. This sections provides an overview and 
documentation for some of those features.

.. _apis:

APIs
----

When configuring Py-Authorize with the `Configuration` global variable, 
you are actually instantiating a single instance of the `authorize_api` 
class. `authorize.Address`, `authorize.BankAccount`, `authorize.CreditCard`, 
`authorize.Customer` and `authorize.Recurring` are all wrappers for 
accessing this globally configured API. You can access the API explicitly 
through the `Configuration.api` class member. For example, to perform a 
basic sale transaction with a credit card using the API you would use the 
following method:

.. code-block:: python

    result = authorize.Configuration.api.transaction.sale({
        'amount': 40.00,
        'credit_card': {
            'card_number': '4111111111111111',
            'expiration_date': '04/2014',
        }
    })

Each `authorize_api` instance contains the following members for performing API 
calls:

- ``api.customer``
- ``api.credit_card``
- ``api.bank_account``
- ``api.address``
- ``api.recurring``
- ``api.batch``
- ``api.transaction``


Multiple Gateway Configurations
-------------------------------

For some payment applications, there may be a need to support multiple 
gateways. With Py-Authorize, you can instantiate any number of payment 
gateway configurations.

Example
~~~~~~~

.. code-block:: python

    configuration_1 = authorize.Configuration(
        Environment.PRODUCTION,
        'api_login_id',
        'api_transaction_key',
    )

    configuration_2 = authorize.Configuration(
        Environment.PRODUCTION,
        'another_api_login_key',
        'another_api_transaction_key',
    )

Once a new configuration has been created, you can make use of each 
configuration object's `api` members as outlined in :ref:`APIs <apis>`


