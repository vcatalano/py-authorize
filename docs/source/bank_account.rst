Bank Accounts
=============

Bank accounts must be associated to a customer profile on the Authorize.net 
server. A bank account can be associated when a new customer is created, to 
see how this is handled refer to the :doc:`Customer API<customer>` 
documentation.

.. note::

    The ability to process transactions from a bank account is not a 
    standard gateway account feature. You must register for eCheck 
    functionality seperately. For more information see `Authorize.net's 
    eCheck documentation`_.

.. _Authorize.net's eCheck documentation: http://www.authorize.net/solutions/merchantsolutions/merchantservices/echeck/


Create
------

To add a bank account to an existing user, the minimal amount of information 
required is the routing number, account number, name on the account and the 
customer profile ID. The customer profile ID is passed as the first argument 
to the ``create`` method.

Minimal Example
~~~~~~~~~~~~~~~

.. code-block:: python

    result = authorize.BankAccount.create('19086684', {
        'routing_number': '322271627',
        'account_number': '00987467838473',
        'name_on_account': 'Rob Otron',
    })

    result.payment_id
    # e.g. '17633593'


Full Example
~~~~~~~~~~~~

When creating a new bank account, the billing address information can also 
be associated to the account.

.. code-block:: python

    result = authorize.BankAccount.create('19086684', {
        'customer_type': 'individual',
        'account_type': 'checking',
        'routing_number': '322271627',
        'account_number': '00987467838473',
        'name_on_account': 'Rob Otron',
        'bank_name': 'Evil Bank Co.',
        'echeck_type': 'CCD',
        'billing': {
            'first_name': 'Rob',
            'last_name': 'Oteron',
            'company': 'Robotron Studios',
            'address': '101 Computer Street',
            'city': 'Tucson',
            'state': 'AZ',
            'zip': '85704',
            'country': 'US',
            'phone_number': '520-123-4567',
            'fax_number': '520-456-7890',
        },
    })

    result.payment_id
    # e.g. '17633614'


Details
-------

The ``details`` method returns the information for a given customer payment 
profile. This method takes both the customer profile ID and customer payment 
profile ID.

The following information is returned in the result attribute dictionary:

- ``payment_profile.payment_id``
- ``payment_profile.customer_type``
- ``payment_profile.payment.bank_account.account_type``
- ``payment_profile.payment.bank_account.routin_number``
- ``payment_profile.payment.bank_account.account_number``
- ``payment_profile.payment.bank_account.name_on_account``
- ``payment_profile.payment.bank_account.bank_name``
- ``payment_profile.payment.bank_account.echeck_type``
- ``payment_profile.bill_to.company``
- ``payment_profile.bill_to.first_name``
- ``payment_profile.bill_to.last_name``
- ``payment_profile.bill_to.address``
- ``payment_profile.bill_to.city``
- ``payment_profile.bill_to.state``
- ``payment_profile.bill_to.zip``
- ``payment_profile.bill_to.country``
- ``payment_profile.bill_to.phone_number``
- ``payment_profile.bill_to.fax_number``

.. code-block:: python

    result = authorize.BankAccount.details('19086684', '17633614')


Update
------

The ``update`` method will update the bank account information for a given 
payment profile ID. The method requires the customer profile ID, the payment 
profile ID and the new bank account information.

.. code-block:: python

    result = authorize.BankAccount.update('19086684', '17633614', {
        'customer_type': 'individual',
        'account_type': 'checking',
        'routing_number': '322271627',
        'account_number': '00987467838473',
        'name_on_account': 'Rob Otron',
        'bank_name': 'Evil Bank Co.',
        'echeck_type': 'CCD',
        'billing': {
            'first_name': 'Rob',
            'last_name': 'Oteron',
            'company': 'Robotron Studios',
            'address': '101 Computer Street',
            'city': 'Tucson',
            'state': 'AZ',
            'zip': '85704',
            'country': 'US',
            'phone_number': '520-123-4567',
            'fax_number': '520-456-7890',
        },
    })


Delete
------

Deleting a customer bank account will remove the payment profile from the 
given customer.

.. code-block:: python

    result = authorize.BankAccount.delete('19086684', '17633319')


Transactions
------------

For information on how to run transactions against stored credit cards, 
please refer to the :doc:`Transaction <transaction>` documentation.
