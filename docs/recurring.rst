Recurring
=========

The Py-Authorize Recurring API is used to integrate with Authorize.net's 
Automated Recurring Billing (ARB) subscription-based payment service. It 
provides all functionality for managing recurring billing against credit 
cards and bank accounts.

Create
------

Authorize.net's ARB service functions seperately from the Customer 
Information Management API. This means you cannot create recurring payments 
for stored customers, credit cards or bank accounts. Instead, you will need 
to provide all customer and payment information explicitly.

Minimal Example
~~~~~~~~~~~~~~~

.. code-block:: python

    result = authorize.Recurring.create({
        'amount': 45.00,
        'interval_length': 1,
        'interval_unit': 'months',
        'credit_card': {
            'card_number': '4111111111111111',
            'expiration_date': '04-2014',
            'card_code': '456',
        },
    })

    # result.subscription_id
    # e.g. '1725604'


In this example, the customer will be charged $45.00 every month until the 
subscription is canceled or the payment gateway can no longer process the 
payment method (e.g. the card has expired). Authorize.net only permits 
interval units of `days` or `years`.

To specify a limited number of occurrences, use the `total_occurrences` 
parameter.

.. code-block:: python

    result = authorize.Recurring.create({
        'amount': 45.00,
        'interval_length': 14,
        'interval_unit': 'days',
        'total_occurrences': 52,
        'credit_card': {
            'card_number': '4111111111111111',
            'expiration_date': '04-2014',
            'card_code': '456',
        },
    })

    # result.subscription_id
    # e.g. '1725605'


Full Example
~~~~~~~~~~~~

Recurring payments can also be configured with customer bank accounts. The 
following example shows all recurring payment parameters available.

.. code-block:: python

    result = authorize.Recurring.create({
        'amount': 45.00,
        'name': 'Ultimate Robot Supreme Plan',
        'total_occurrences': 30,
        'interval_length': 2,
        'interval_unit': 'months',
        'trial_amount': 30.00,
        'trial_occurrences': 2,
        'bank_account': {
            'customer_type': 'individual',
            'account_type': 'checking',
            'routing_number': '322271627',
            'account_number': '00987467838473',
            'name_on_account': 'Rob Otron',
            'bank_name': 'Evil Bank Co.',
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
        'order': {
            'invoice_number': 'INV0001',
            'description': 'Just another invoice...',
        },
        'customer': {
            'merchant_id': '1234567890',
            'email': 'rob@robotronstudios.com',
            'description': 'I am a robot',
        },
    })

    # result.subscription_id
    # e.g. '1725628'


Details
-------

To the get the status of a recurring payment, use the `details` method.

.. code-block:: python

    result = authorize.Recurring.details('1725628')

    # result.status
    # e.g. 'active'


Update
------

The `update` method takes the same parameters as the `create` method. 
However, once recurring payments have started, there are certain exceptions.

- The subscription `start_date` may only be updated if no successful 
  payments have been completed.
- The subscription `interval_length` and `interval_unit` may not be updated. 
  Instead, you must create a new subscription if you want different values 
  for these parameters.
- The number of `trial_occurrences` may only be updated if the subscription 
  has not yet begun or is still in the trial period.
- If the `start_date` is the 31st, and the interval is monthly, the billing 
  date is the last day of each month (even when the month does not have 31 
  days).


When updating a recurring payment, you must pass in the subscription ID of 
the payment you wish to update along with the new subscription information.

.. code-block:: python

    result = authorize.Recurring.update('1725628', {
        'name': 'Ultimate Robot Supreme Plan',
        'amount': 45.00,
        'total_occurrences': 30,
        'trial_amount': 30.00,
        'trial_occurrences': 2,
        'credit_card': {
            'card_number': '4111111111111111',
            'expiration_date': '04-2014',
            'card_code': '456',
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
        'order': {
            'invoice_number': 'INV0001',
            'description': 'Just another invoice...',
        },
        'customer': {
            'merchant_id': '1234567890',
            'email': 'rob@robotronstudios.com',
            'description': 'I am a robot',
        },
    })


Cancel
------

To cancel a recurring payment, pass the subscription ID to the `cancel` 
method.

.. code-block:: python

    authorize.Recurring.delete('1725628')





