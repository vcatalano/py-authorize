Credit Cards
============

Credit cards must be associated to a customer profile on the Authorize.net 
server. A credit card can be associated when a new customer is created, to 
see how this is handled refer to the :doc:`Customer API<customer>` 
documentation.

Create
------

To add a credit card to an existing user, the minimal amount of information 
required is the credit card number, the expiration date and the customer 
profile ID. The customer profile ID is passed as the first argument to the 
``create`` method.

Minimal Example
~~~~~~~~~~~~~~~

.. code-block:: python

    result = authorize.CreditCard.create('19086684', {
        'card_number': '4111111111111111',
        'expiration_date': '04/2014',
    })

    result.payment_id
    # e.g. '17633318'

When creating a new credit card, the expiration month and date can be 
seperate values.

.. code-block:: python

    result = authorize.CreditCard.create('19086684', {
        'card_number': '4111111111111111',
        'expiration_month': '04',
        'expiration_year': '2014',
    })

    result.payment_id
    # e.g. '17633319'


Full Example
~~~~~~~~~~~~

When creating a new credit card, the billing address information can also be 
associated to the card.

.. code-block:: python

    result = authorize.CreditCard.create('19086684', {
        'customer_type': 'individual',
        'card_number': '4111111111111111',
        'expiration_month': '04',
        'expiration_year': '2014',
        'card_code': '123',
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
    # e.g. '17633319'


Details
-------

The ``details`` method returns the information for a given customer payment 
profile. This method takes both the customer profile ID and customer payment 
profile ID.

The following information is returned in the result attribute dictionary:

- ``payment_profile.payment_id``
- ``payment_profile.customer_type``
- ``payment_profile.payment.credit_card.card_number``
- ``payment_profile.payment.credit_card.expiration_date``
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

    result = authorize.CreditCard.details('19086684', '17633319')


Update
------

The ``update`` method will update the credit card information for a given 
payment profile ID. The method requires the customer profile ID, the payment 
profile ID and the new credit card information.

.. code-block:: python

    result = authorize.CreditCard.update('19086684', '17633319', {
        'customer_type': 'individual',
        'card_number': '4111111111111111',
        'expiration_month': '04',
        'expiration_year': '2014',
        'card_code': '123',
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

Deleting a customer credit card will remove the payment profile from the 
given customer.

.. code-block:: python

    result = authorize.CreditCard.delete('19086684', '17633319')


Validate
--------

Stored credit cards can be validated before attempting to run a transaction 
against them.

.. code-block:: python

    result = authorize.CreditCard.validate('19086684', '17633319', {
        'card_code': '123',
        'validationMode': 'liveMode'
    })


Transactions
------------

For information on how to run transactions agains stored credit cards, 
please refer to the :doc:`Transaction <transaction>` documentation.
