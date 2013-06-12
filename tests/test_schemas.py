from authorize.schemas import AddressSchema
from authorize.schemas import BankAccountSchema
from authorize.schemas import CreditCardSchema
from authorize.schemas import CreateRecurringSchema

from colander import Invalid
from datetime import date
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
    'phone_number': '520-1234567',
    'fax_number': '520-765-4321',
}

BASIC_RECURRING = {
    'amount': 40,
    'interval_length': 14,
    'interval_unit': 'days',
    'credit_card': {
        'card_number': '4111111111111111',
        'expiration_date': '04/{0}'.format(date.today().year + 1),
    },
}

INVALID_ADDRESS = {
    'city': 'Tucson',
    'state': 'AZ',
    'zip': '85704',
    'country': 'US',
}

CREDIT_CARD_EXP_MONTH_AND_YEAR = {
    'card_number': '4111111111111111',
    'card_code': '456',
    'expiration_month': '04',
    'expiration_year': str(date.today().year + 1)
}

CREDIT_CARD_EXP_DATE = {
    'card_number': '4111111111111111',
    'card_code': '456',
    'expiration_date': '04/{0}'.format(date.today().year + 1),
}

INVALID_CREDIT_CARD_NUMBER = {
    'card_number': 'Bad card number',
    'card_code': '456',
    'expiration_date': '04/{0}'.format(date.today().year + 1),
}

INVALID_CREDIT_CARD_NO_EXP_DATE = {
    'card_number': '4111111111111111',
    'card_code': '456',
}

INVALID_CREDIT_CARD_NO_YEAR = {
    'card_number': '4111111111111111',
    'card_code': '456',
    'expiration_month': '04',
}

INVALID_CREDIT_CARD_NO_MONTH = {
    'card_number': '4111111111111111',
    'card_code': '456',
    'expiration_year': str(date.today().year + 1),
}

FULL_CREDIT_CARD = {
    'card_number': '4111111111111111',
    'card_code': '456',
    'expiration_month': '04',
    'expiration_year': str(date.today().year + 1),
    'first_name': 'Rob',
    'last_name': 'Oteron',
}

BASIC_BANK_ACCOUNT = {
    'routing_number': '322271627',
    'account_number': '00987467838473',
    'name_on_account': 'Rob Otron',
}

FULL_BANK_ACCOUNT = {
    'account_type': 'checking',
    'routing_number': '322271627',
    'account_number': '00987467838473',
    'name_on_account': 'Rob Otron',
    'bank_name': 'Evil Bank Co.',
    'echeck_type': 'CCD',
}

INVALID_BANK_ACCOUNT_BAD_ROUTING_NUMBER = {
    'routing_number': 'Bad routing number',
    'account_number': '00987467838473',
    'name_on_account': 'Rob Otron',
}

INVALID_BANK_ACCOUNT_BAD_ACCOUNT_NUMBER = {
    'routing_number': '322271627',
    'account_number': 'Bad account number',
    'name_on_account': 'Rob Otron',
}


class SchemaTests(TestCase):

    maxDiff = None

    def test_address_schema(self):
        schema = AddressSchema()
        schema.deserialize(ADDRESS)

    def test_credit_card_schema(self):
        schema = CreditCardSchema()
        schema.deserialize(CREDIT_CARD_EXP_MONTH_AND_YEAR)
        schema.deserialize(CREDIT_CARD_EXP_DATE)
        self.assertRaises(Invalid, schema.deserialize, INVALID_CREDIT_CARD_NUMBER)
        self.assertRaises(Invalid, schema.deserialize, INVALID_CREDIT_CARD_NO_EXP_DATE)
        self.assertRaises(Invalid, schema.deserialize, INVALID_CREDIT_CARD_NO_MONTH)
        schema.deserialize(FULL_CREDIT_CARD)

    def test_bank_account_schema(self):
        schema = BankAccountSchema()
        schema.deserialize(BASIC_BANK_ACCOUNT)
        schema.deserialize(FULL_BANK_ACCOUNT)
        self.assertRaises(Invalid, schema.deserialize, INVALID_BANK_ACCOUNT_BAD_ROUTING_NUMBER)
        self.assertRaises(Invalid, schema.deserialize, INVALID_BANK_ACCOUNT_BAD_ACCOUNT_NUMBER)

    def test_arb_address_schema(self):
        schema = CreateRecurringSchema().bind(arb=True)
        schema.deserialize(BASIC_RECURRING)
