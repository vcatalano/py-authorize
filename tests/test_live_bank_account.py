from authorize import BankAccount
from authorize import Customer
from authorize import AuthorizeResponseError

from nose.plugins.attrib import attr

from unittest import TestCase

BANK_ACCOUNT = {
    'routing_number': '322271627',
    'account_number': '00987467838473',
    'name_on_account': 'Rob Otron',
}

FULL_BANK_ACCOUNT = {
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
}

PAYMENT_RESULT = {
    'bank_account': {
        'routing_number': 'XXXX1627',
        'account_number': 'XXXX8473',
        'name_on_account': 'Rob Otron',
        'echeck_type': 'WEB',
    }
}


@attr('live_tests')
class BankAccountTests(TestCase):

    def test_live_bank_account(self):
        # Create a customer so that we can test payment creation against him
        result = Customer.create()
        customer_id = result.customer_id

        # Create a new bank account
        result = BankAccount.create(customer_id, BANK_ACCOUNT)
        payment_id = result.payment_id

        # Read credit card data
        result = BankAccount.details(customer_id, payment_id)
        self.assertEquals(PAYMENT_RESULT, result.payment_profile.payment)

        # Update credit card
        BankAccount.update(customer_id, payment_id, BANK_ACCOUNT)

        # Delete tests
        BankAccount.delete(customer_id, payment_id)
        self.assertRaises(AuthorizeResponseError, BankAccount.delete, customer_id, payment_id)

    def test_live_full_bank_account(self):
        # Create a customer so that we can test payment creation against him
        result = Customer.create()
        customer_id = result.customer_id

        # Create a new bank account
        result = BankAccount.create(customer_id, FULL_BANK_ACCOUNT)
        payment_id = result.payment_id

        # Make sure the billing address we set is the same we get back
        result = BankAccount.details(customer_id, payment_id)
        self.assertEquals(FULL_BANK_ACCOUNT['billing'], result.payment_profile.bill_to)
