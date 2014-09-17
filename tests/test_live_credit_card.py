from authorize import CreditCard
from authorize import Customer
from authorize import AuthorizeResponseError

from datetime import date

from nose.plugins.attrib import attr

from unittest import TestCase

CREDIT_CARD = {
    'card_number': '4111111111111111',
    'expiration_date': '04/{0}'.format(date.today().year + 1),
    'card_code': '456',
}

MASKED_CREDIT_CARD = {
    'card_number': 'XXXX1111',
    'expiration_date': '05/{0}'.format(date.today().year+2),
    'card_code': '789'
}

FULL_CREDIT_CARD = {
    'card_number': '4111111111111111',
    'expiration_date': '04/{0}'.format(date.today().year + 1),
    'card_code': '456',
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
    'credit_card': {
        'card_number': 'XXXX1111',
        'expiration_date': 'XXXX',
    }
}


@attr('live_tests')
class CreditCardTests(TestCase):

    def test_live_basic_credit_card(self):
        # Create a customer so that we can test payment creation against him
        result = Customer.create()
        customer_id = result.customer_id

        # Create a new credit card
        result = CreditCard.create(customer_id, CREDIT_CARD)
        payment_id = result.payment_id

        # Attempt to create a duplicate credit card entry. This will fail
        # since it is a duplicate payment method.
        self.assertRaises(AuthorizeResponseError, CreditCard.create, customer_id, CREDIT_CARD)

        # Read credit card data
        result = CreditCard.details(customer_id, payment_id)
        self.assertEquals(PAYMENT_RESULT, result.payment_profile.payment)

        # Update credit card
        CreditCard.update(customer_id, payment_id, CREDIT_CARD)

        # Update with masked number
        CreditCard.update(customer_id, payment_id, MASKED_CREDIT_CARD)

        # Delete tests
        CreditCard.delete(customer_id, payment_id)
        self.assertRaises(AuthorizeResponseError, CreditCard.delete, customer_id, payment_id)

    def test_live_full_credit_card(self):
        # Create a customer so that we can test payment creation against him
        result = Customer.create()
        customer_id = result.customer_id

        result = CreditCard.create(customer_id, FULL_CREDIT_CARD)
        payment_id = result.payment_id

        # Make sure the billing address we set is the same we get back
        result = CreditCard.details(customer_id, payment_id)
        self.assertEquals(FULL_CREDIT_CARD['billing'], result.payment_profile.bill_to)

        # Validate the credit card information
        result = CreditCard.validate(customer_id, payment_id, {
            'card_code': '456',
            'validation_mode': 'testMode',
        })
