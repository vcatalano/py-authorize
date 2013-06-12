from authorize import Address
from authorize import Customer
from authorize import AuthorizeResponseError

from nose.plugins.attrib import attr

from unittest2 import TestCase

ADDRESS = {
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


@attr('live_tests')
class AddressTests(TestCase):

    def test_live_address(self):
        # Create a customer so that we can test payment creation against him
        result = Customer.create()
        customer_id = result.customer_id

        # Create a new shipping address
        result = Address.create(customer_id, ADDRESS)
        address_id = result.address_id

        result = Address.details(customer_id, address_id)
        # Compare the address without the customer_address_id
        del result.address['address_id']
        self.assertEquals(ADDRESS, result.address)

        Address.update(customer_id, address_id, ADDRESS)

        # Delete the address and make sure it is deleted by attempting to
        # delete it again.
        Address.delete(customer_id, address_id)
        self.assertRaises(AuthorizeResponseError, Address.delete, customer_id, address_id)
