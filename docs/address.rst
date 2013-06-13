Address
=======

The Address API manages customer shipping addresses for Authorize.net's 
Customer Information Manager (CIM). Addresses must be associated to a 
customer profile on the Authorize.net server. An address can be associated 
when a new customer is created, to see how this is handled refer to the 
:doc:`Customer API<customer>` documentation.

Create
------

To associate an address to an existing customer use the `create` method. 
When creating an address, you must provide the customer profile ID as the 
first argument. No fields are required when creating an address, however, at 
least one field must be provided.

.. code-block:: python

    result = authorize.Address.create('19086684', {
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
    })

    result.address_id
    # e.g. '17769620'


Details
-------

The `details` method returns the information for a given customer address. 
You must provide the both customer profile ID and the customer address ID 
respectively.

The following information is returnd in the result attribute dictionary:

- ``address.first_name``
- ``address.last_name``
- ``address.company``
- ``address.address``
- ``address.city``
- ``address.state``
- ``address.zip``
- ``address.country``
- ``address.phone_number``
- ``address.fax_number``

.. code-block:: python

    result = authorize.Address.details('19086684', '17769620')

    result.address_id
    # e.g. '17769620'


Update
------

The ``update`` method will update the address information for a given 
address ID. The method requires the customer profile ID, the customer 
address ID and the updated customer address information.

.. code-block:: python

    result = authorize.Address.create('19086684', '17769620', {
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
    })


Delete
------

Deleting a customer address will remove the address information associated 
the customer.

.. code-block:: python

    authorize.Address.delete('19086684', '17769620')