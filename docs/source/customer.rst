Customer
========

The ``Customer`` class provides an interface to Authorize.net's Customer
Information Manager (CIM) API.

Create
------

When creating a customer profile, no information is actually needed. A random 
merchant ID is associated to the customer if none is provided. Once a user 
been created, address and payment information can then be associated to the 
profile.

Minimal Example
~~~~~~~~~~~~~~~

.. code-block:: python

    result = authorize.Customer.create()

    result.customer_id
    # e.g. '19086351'


Creating Profile with Basic Information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    result = authorize.Customer.create({
        'email': 'rob@robotronstudios.com',
        'description': 'Rob the robot',
        'customer_type': 'individual',
    })

    result.customer_id
    # e.g. '19086352'


Full Example
~~~~~~~~~~~~

When creating a customer, additional shipping address and payment information 
can be provided as well.

.. code-block:: python

    result = authorize.Customer.create({
        'merchant_id': '8989762983402603',
        'email': 'rob@robotronstudios.com',
        'description': 'Rob the robot',
        'customer_type': 'individual',
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
        'credit_card': {
            'card_number': '4111111111111111',
            'card_code': '456',
            'expiration_month': '04',
            'expiration_year': '2014',
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
            'phone_number': '520-123-4567',
            'fax_number': '520-456-7890',
        }
    })

    result.customer_id
    # e.g. '19086352'


Details
-------

The ``details`` method returns the information for a given customer profile 
based on the customer ID.

The following information is returned in the result attribute dictionary:

- ``profile.merchant_id``
- ``profile.email``
- ``profile.description``
- ``profile.customer_type``
- ``address_ids``
- ``payment_ids``

.. code-block:: python

    result = authorize.Customer.details('19086352')


Update
------

Customer profile information can be easily updated on the server.

.. code-block:: python

    result = authorize.Customer.update('19086352', {
        'email': 'rob@robotronstudios.com',
        'description': 'Rob the robot',
        'customer_type': 'individual',
    })


Delete
------

Deleting a customer will delete the customer profile along with all stored 
addresses and billing information.

.. code-block:: python

    result = authorize.Customer.delete('19086352')


List
----

The ``list`` method returns a list of all customer profile IDs.

.. code-block:: python

    result = authorize.Customer.list()

    result.profile_ids
    # e.g. ['16467005', '16467010', '16467092', '17556329']

