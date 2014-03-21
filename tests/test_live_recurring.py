import random

from authorize import Recurring
from authorize import AuthorizeResponseError

from datetime import date

from nose.plugins.attrib import attr

from unittest import TestCase

BASIC_RECURRING = {
    'interval_length': 14,
    'interval_unit': 'days',
    'credit_card': {
        'card_number': '4111111111111111',
        'expiration_date': '04/{0}'.format(date.today().year + 1),
    },
}

CREATE_RECURRING = {
    'name': 'Ultimate Robot Supreme Plan',
    'total_occurrences': 30,
    'interval_length': 2,
    'interval_unit': 'months',
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
}


# When updating a subscription the only parameters we cannot update are the
# interval unit and interval length
UPDATE_RECURRING = {
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
}


@attr('live_tests')
class RecurringTests(TestCase):

    def test_live_recurring(self):
        # Create a new recurring subscription. The amount needs to be random,
        # otherwise the subscription will register as a duplicate
        recurring = CREATE_RECURRING.copy()
        recurring['amount'] = random.randrange(100, 100000) / 100.0
        Recurring.create(recurring)

        # An error will occur if we attempt to create a duplicate
        # subscription
        self.assertRaises(AuthorizeResponseError, Recurring.create, recurring)

        recurring = BASIC_RECURRING.copy()
        recurring['amount'] = random.randrange(100, 100000) / 100.0
        result = Recurring.create(recurring)

        # Read subscription status
        Recurring.details(result.subscription_id)

        # Update subscription information
        Recurring.update(result.subscription_id, UPDATE_RECURRING)

        # Cancel (delete) the subscription
        Recurring.delete(result.subscription_id)
