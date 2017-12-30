Transactions
============

The primary purpose for any payment gateway is to provide functionality for 
taking payments for goods or services and charging a consumer. Py-Authorize's 
Transaction API provides all the functionality developers will need for all 
situations when developing a payment system. 

Sale
----

The most common transaction type for credit cards is a ''sale''. During the 
transaction, the credit card is first authorized for the given transaction 
amount, if approved, it is automattically submitted for settlement.

.. note::

    When performing a ``sale`` transaction, Py-Authorize is actually 
    performing an ``authCapture``.

Minimal Example
~~~~~~~~~~~~~~~

.. code-block:: python

    result = authorize.Transaction.sale({
        'amount': 40.00,
        'credit_card': {
            'card_number': '4111111111111111',
            'expiration_date': '04/2014',
        }
    })

    result.transaction_response.trans_id
    # e.g. '2194343352'


Py-Authorize fully supports all Authorize.net gateway parameters for 
transactions.

Full Example
~~~~~~~~~~~~

.. code-block:: python

    result = authorize.Transaction.sale({
        'amount': 56.00,
        'email': 'rob@robotronstudios.com',
        'credit_card': {
            'card_number': '4111111111111111',
            'card_code': '523',
            'expiration_date': '04/2014',
        },
        'shipping': {
            'first_name': 'Rob',
            'last_name': 'Oteron',
            'company': 'Robotron Studios',
            'address': '101 Computer Street',
            'city': 'Tucson',
            'state': 'AZ',
            'zip': '85704',
            'country': 'US',
        },
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
        'tax': {
            'amount': 4.00,
            'name': 'Double Taxation Tax',
            'description': 'Another tax for paying double tax',
        },
        'duty': {
            'amount': 2.00,
            'name': 'The amount for duty',
            'description': 'I can''t believe you would pay for duty',
        },
        'line_items': [{
            'item_id': 'CIR0001',
            'name': 'Circuit Board',
            'description': 'A brand new robot component',
            'quantity': 5,
            'unit_price': 4.00,
            'taxable': 'true',
        }, {
            'item_id': 'CIR0002',
            'name': 'Circuit Board 2.0',
            'description': 'Another new robot component',
            'quantity': 1,
            'unit_price': 10.00,
            'taxable': 'true',
        }, {
            'item_id': 'SCRDRVR',
            'name': 'Screwdriver',
            'description': 'A basic screwdriver',
            'quantity': 1,
            'unit_price': 10.00,
            'taxable': 'true',
        }],
        'user_fields': [{
            'name': 'additionalDescription',
            'value': 'An additional description goes here...'
        }, {
            'name': 'moreInfo',
            'value': 'This is some more information...'
        }]
        'order': {
            'invoice_number': 'INV0001',
            'description': 'Just another invoice...',
        },
        'shipping_and_handling': {
            'amount': 10.00,
            'name': 'UPS 2-Day Shipping',
            'description': 'Handle with care',
        },
        'extra_options': {
            'customer_ip': '100.0.0.1',
        },
        'retail': {
            'market_type':0,
            'device_type':7,
        },
        'tax_exempt': False,
        'recurring': True,
    })

    result.transaction_response.trans_id
    # e.g. '2194343353'


Card Present Example
~~~~~~~~~~~~~~~~~~~~

If doing a card present transaction, track data can be passed in instead of a parsed credit card.

.. note::

    It may still be useful to parse the track data in application logic to verify expiration date or card issuer.

.. code-block:: python

    result = authorize.Transaction.sale({
        'amount': 40.00,
        'track_data': {
            'track_1': '%B4111111111111111^OTERON/ROB^14041010300523300000000000000000000000000000000?',
        }
    })

    result.transaction_response.trans_id
    # e.g. '2194343352'


Minimal Bank Account Transaction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Transactions can also be ran against bank accounts.

.. warning::

    Since bank account (eCheck.net) transactions are handled differently from 
    credit card transactions, you should avoid using the `auth` method when 
    dealing with bank accounts. Only use the `sale` method when processing 
    payments.

.. code-block:: python

    result = authorize.Transaction.sale({
        'amount': 40.00,
        'bank_account': {
            'routing_number': '322271627',
            'account_number': '00987467838473',
            'name_on_account': 'Rob Otron',
        },
    })

    result.transaction_response.trans_id
    # e.g. '2194343357'


Full Transactions with Bank Accounts
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    result = authorize.Transaction.sale({
        'amount': 56.00,
        'email': 'rob@robotronstudios.com',
        'bank_account': {
            'customer_type': 'individual',
            'account_type': 'checking',
            'routing_number': '322271627',
            'account_number': '00987467838473',
            'name_on_account': 'Rob Otron',
            'bank_name': 'Evil Bank Co.',
            'echeck_type': 'WEB',
        },
        'shipping': {
            'first_name': 'Rob',
            'last_name': 'Oteron',
            'company': 'Robotron Studios',
            'address': '101 Computer Street',
            'city': 'Tucson',
            'state': 'AZ',
            'zip': '85704',
            'country': 'US',
        },
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
        'tax': {
            'amount': 4.00,
            'name': 'Double Taxation Tax',
            'description': 'Another tax for paying double tax',
        },
        'duty': {
            'amount': 2.00,
            'name': 'The amount for duty',
            'description': 'I can''t believe you would pay for duty',
        },
        'line_items': [{
                'item_id': 'CIR0001',
                'name': 'Circuit Board',
                'description': 'A brand new robot component',
                'quantity': 5,
                'unit_price': 4.00,
                'taxable': 'true',
            }, {
                'item_id': 'CIR0002',
                'name': 'Circuit Board 2.0',
                'description': 'Another new robot component',
                'quantity': 1,
                'unit_price': 10.00,
                'taxable': 'true',
            }, {
                'item_id': 'SCRDRVR',
                'name': 'Screwdriver',
                'description': 'A basic screwdriver',
                'quantity': 1,
                'unit_price': 10.00,
                'taxable': 'true',
            }],
        'order': {
            'invoice_number': 'INV0001',
            'description': 'Just another invoice...',
        },
        'shipping_and_handling': {
            'amount': 10.00,
            'name': 'UPS 2-Day Shipping',
            'description': 'Handle with care',
        },
        'extra_options': {
            'customer_ip': '100.0.0.1',
        },
        'tax_exempt': False,
        'recurring': True,
    })

    result.transaction_response.trans_id
    # e.g. '2194343358'


Transactions with CIM Data
~~~~~~~~~~~~~~~~~~~~~~~~~~

Transactions can also be ran with stored customer payment profile 
information. When performing a transaction for a CIM managed payment profile, 
you must include the customer ID and payment profile ID. Additionally, you 
can include a customer's stored address ID as the shipping address for an 
order.

.. code-block:: python

    result = authorize.Transaction.sale({
        'amount': 56.00,
        'customer_id': '19086684',
        'payment_id': '17633614',
        'shipping_id': '14634122',
    })

    result.transaction_response.trans_id
    # e.g. '2194343354'


Full Transactions Example with CIM Data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    result = authorize.Transaction.sale({
        'amount': 56.00,
        'customer_id': '19086684',
        'payment_id': '17633614',
        'shipping_id': '14634122',
        'tax': {
            'amount': 4.00,
            'name': 'Double Taxation Tax',
            'description': 'Another tax for paying double tax',
        },
        'duty': {
            'amount': 2.00,
            'name': 'The amount for duty',
            'description': 'I can''t believe you would pay for duty',
        },
        'line_items': [{
                'item_id': 'CIR0001',
                'name': 'Circuit Board',
                'description': 'A brand new robot component',
                'quantity': 5,
                'unit_price': 4.00,
                'taxable': 'true',
            }, {
                'item_id': 'CIR0002',
                'name': 'Circuit Board 2.0',
                'description': 'Another new robot component',
                'quantity': 1,
                'unit_price': 10.00,
                'taxable': 'true',
            }, {
                'item_id': 'SCRDRVR',
                'name': 'Screwdriver',
                'description': 'A basic screwdriver',
                'quantity': 1,
                'unit_price': 10.00,
                'taxable': 'true',
            }],
        'order': {
            'invoice_number': 'INV0001',
            'description': 'Just another invoice...',
            'order_number': 'PONUM00001',
        },
        'shipping_and_handling': {
            'amount': 10.00,
            'name': 'UPS 2-Day Shipping',
            'description': 'Handle with care',
        },
        'extra_options': {
            'customer_ip': '100.0.0.1',
        },
        'tax_exempt': False,,
        'recurring': True,
    })

    result.transaction_response.trans_id
    # e.g. '2194343355'


.. note::

    The `email` field cannot be used in combination with the `customer_id`
    field. If the `customer_id` field is provided, the `email` field will
    be ignored during the transaction processing.

Auth
----

The ``auth`` method is equivalent to the the Authorize.net ``authorizeOnly`` 
method. When calling ``auth``, the credit card is temporarily authorized for 
the given transaction amount without being submitted for settlement. This 
allows you to ensure you will be able to charge the card but hold off if in 
case you later no longer need to charge the card or need reduce the amount 
you plan to charge. In order to finalize the transaction charge, you must 
settle the transaction by using the ``settle`` transaction method.

This method takes the same parameters as the ``sale`` method.

Example
~~~~~~~

.. code-block:: python

    result = authorize.Transaction.auth({
        'amount': 40.00,
        'credit_card': {
            'card_number': '4111111111111111',
            'expiration_date': '04/2014,
        }
    })

    result.transaction_response.trans_id
    # e.g. '2194343356'

The ``auth`` method takes the same values as as the ``sale`` method.

Settling
--------

In order to finalize a previously authorized transaction, you must call the
``settle`` method with the transaction ID. When settling a transaction, the 
amount for the transaction can be changed as long as it is less than the
original authorized amount.

Example
~~~~~~~ 

.. code-block:: python

    result = authorize.Transaction.settle('89798235')

The amount is not required if you want to settle the authorized amount. To
settle a different amount, pass the amout as the second parameter.

.. code-block:: python

    result = authorize.Transaction.settle('89798235', 20.00)

Refund
------

This transaction type is used to refund a customer for a transaction that was
originally processed and successfully settled through the payment gateway (it
is the Authorize.net equivalent of a Credit).

When issuing a refund, Authorize.net requires the amount of the transaction,
the last four digits of the credit card and the transaction ID. If you do not 
have the amount or last four digits of the credit card readily available, 
this information can be gotten using the ``details`` method.

Example
~~~~~~~

.. code-block:: python

    result = authorize.Transaction.refund({
        'amount': 40.00,
        'last_four': '1111',
        'transaction_id': '0123456789',
        'order': {
            'invoice_number': 'INV0001',
            'description': 'Just another invoice...',
            'order_number': 'PONUM00001',
        }
    })


.. _void:

Void
----

This transaction type can be used to cancel either an original transaction 
that is not yet settled or an entire order composed of more than one 
transaction. A Void prevents the transaction or the order from being sent 
for settlement. You will only be able to void a transaction that is not 
already settled, expired, or failed.

Example
~~~~~~~

.. code-block:: python

    result = authorize.Transaction.void('0123456789')


Credit
------

Authorize.net provides the ability to issue refunds for transactions that 
were not originally submitted through the payment gateway (it is the 
Authorize.net equivalent of an Unlinked Credit). It also allows you to 
override restrictions set on basic credits, such as refunds for transactions 
beyond the 120-day refund limit.

.. note::

    The ability to submit unlinked credits is not a standard payment 
    gateway account feature. You must request the Expanded Credits 
    Capability (ECC) feature by submitting an application to Authorize.net. 
    More information on Unlinked Credits can be found under `Authorize.net 
    Transaction Types`_ documentation.

Example
~~~~~~~

.. code-block:: python

    result = authorize.Transaction.credit({
        'amount': 120.00,
        'customer_id': '0987654321',
        'payment_id': '1348979152'
    })


.. _Authorize.net Transaction Types: http://www.authorize.net/support/merchant/Submitting_Transactions/Credit_Card_Transaction_Types.htm#Unlinked


Details
-------

This transaction type is used to get detailed information about one specific 
transaction based on the transaction ID.

Example
~~~~~~~

.. code-block:: python

    result = authorize.Transaction.details('0123456789')


List Transactions
-----------------

This transaction type will return data for all transactions in a given batch.

Example
~~~~~~~

.. code-block:: python

    result = authorize.Transaction.list('0123456789')


Additionally, omitting the batch ID will return data for all transactions 
that are currently unsettled.

Example
~~~~~~~

.. code-block:: python

    result = authorize.Transaction.list()

