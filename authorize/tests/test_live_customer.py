from authorize import Customer
from authorize import AuthorizeResponseError

from datetime import date

from nose.plugins.attrib import attr

from unittest2 import TestCase

FULL_CUSTOMER = {
    'email': 'vincent@vincentcatalano.com',
    'description': 'Cool web developer guy',
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
    'bank_account': {
        'routing_number': '322271627',
        'account_number': '00987467838473',
        'name_on_account': 'Rob Otron',
        'bank_name': 'Evil Bank Co.',
        'echeck_type': 'CCD'
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
}

CUSTOMER_WITH_CARD = {
    'email': 'vincent@vincentcatalano.com',
    'description': 'Cool web developer guy',
    'credit_card': {
        'card_number': '4111111111111111',
        'expiration_date': '04/{0}'.format(date.today().year + 1),
        'card_code': '456',
    },
}


@attr('live_tests')
class CustomerTests(TestCase):

    def test_live_customer(self):
        # Create customers
        result = Customer.create()
        Customer.create(FULL_CUSTOMER)
        Customer.create(CUSTOMER_WITH_CARD)

        # Read customer information. This returns the payment profile IDs
        # address IDs for the user
        customer_id = result.customer_id
        Customer.details(customer_id)

        # Update customer information
        Customer.update(customer_id, {
            'email': 'vincent@test.com',
            'description': 'Cool web developer guy'
        })

        # Delete customer information
        Customer.delete(customer_id)
        self.assertRaises(AuthorizeResponseError, Customer.delete, customer_id)

        Customer.list()
