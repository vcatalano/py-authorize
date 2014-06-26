import random

from authorize import Customer
from authorize import Transaction
from authorize import AuthorizeResponseError

from datetime import date, timedelta

from nose.plugins.attrib import attr

from unittest import TestCase

FULL_CARD_NOT_PRESENT_TRANSACTION = {
    'credit_card': {
        'card_number': '4111111111111111',
        'card_code': '523',
        'expiration_month': '04',
        'expiration_year': date.today().year + 1,
    },
    'email': 'rob@robotronstudios.com',
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
        'amount': 45.00,
        'name': 'Double Taxation Tax',
        'description': 'Another tax for paying double tax',
    },
    'duty': {
        'amount': 90.00,
        'name': 'The amount for duty',
        'description': 'I can''t believe you would pay for duty',
    },
    'line_items': [{
        'item_id': 'CIR0001',
        'name': 'Circuit Board',
        'description': 'A brand new robot component',
        'quantity': 5,
        'unit_price': 99.99,
        'taxable': 'true',
    }, {
        'item_id': 'CIR0002',
        'name': 'Circuit Board 2.0',
        'description': 'Another new robot component',
        'quantity': 1,
        'unit_price': 86.99,
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
}

FULL_CARD_PRESENT_TRANSACTION = {
    'track_data': {
        'track_1': "%B4111111111111111^OTERON/ROB^{0:%y%m}101^?".format(date.today() + timedelta(days=365)),
        'track_2': ";4111111111111111={0:%y%m}101?".format(date.today() + timedelta(days=365)),
    },
    'retail': {
        'market_type': 2,
        'device_type': 1,
    },
    'email': 'rob@robotronstudios.com',
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
        'amount': 45.00,
        'name': 'Double Taxation Tax',
        'description': 'Another tax for paying double tax',
    },
    'duty': {
        'amount': 90.00,
        'name': 'The amount for duty',
        'description': 'I can''t believe you would pay for duty',
    },
    'line_items': [{
        'item_id': 'CIR0001',
        'name': 'Circuit Board',
        'description': 'A brand new robot component',
        'quantity': 5,
        'unit_price': 99.99,
        'taxable': 'true',
    }, {
        'item_id': 'CIR0002',
        'name': 'Circuit Board 2.0',
        'description': 'Another new robot component',
        'quantity': 1,
        'unit_price': 86.99,
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
}

CREDIT_CARD = {
    'card_number': '4111111111111111',
    'expiration_date': '04/{0}'.format(date.today().year + 1),
    'card_code': '343',
}

FULL_CIM_TRANSACTION = {
    'amount': 30.00,
    'line_items': [{
        'item_id': 'CIR0001',
        'name': 'Circuit Board',
        'description': 'A brand new robot component',
        'quantity': 5,
        'unit_price': 99.99,
        'taxable': True,
    }, {
        'item_id': 'CIR0002',
        'name': 'Circuit Board 2.0',
        'description': 'Another new robot component',
        'quantity': 1,
        'unit_price': 86.99,
        'taxable': True,
    }, {
        'item_id': 'SCRDRVR',
        'name': 'Screwdriver',
        'description': 'A basic screwdriver',
        'quantity': 1,
        'unit_price': 10.00,
        'taxable': True,
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
    'tax': {
        'amount': 45.00,
        'name': 'Double Taxation Tax',
        'description': 'Another tax for paying double tax',
    },
    'duty': {
        'amount': 90.00,
        'name': 'The amount for duty',
        'description': 'I can''t believe you would pay for duty',
    },
    'extra_options': {
        'customer_ip': 'fe80::f4b6:2a88:70fa:f09f',
    },
    'tax_exempt': False,
    'recurring': True,
    'card_code': '443',
}

FULL_ACCOUNT_TRANSACTION = {
    'bank_account': {
        'customer_type': 'individual',
        'account_type': 'checking',
        'routing_number': '322271627',
        'account_number': '00987467838473',
        'name_on_account': 'Rob Otron',
        'bank_name': 'Evil Bank Co.',
        'echeck_type': 'CCD',
    },
    'email': 'rob@robotronstudios.com',
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
        'amount': 45.00,
        'name': 'Double Taxation Tax',
        'description': 'Another tax for paying double tax',
    },
    'duty': {
        'amount': 90.00,
        'name': 'The amount for duty',
        'description': 'I can''t believe you would pay for duty',
    },
    'line_items': [{
        'item_id': 'CIR0001',
        'name': 'Circuit Board',
        'description': 'A brand new robot component',
        'quantity': 5,
        'unit_price': 99.99,
        'taxable': 'true',
    }, {
        'item_id': 'CIR0002',
        'name': 'Circuit Board 2.0',
        'description': 'Another new robot component',
        'quantity': 1,
        'unit_price': 86.99,
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
}

BANK_ACCOUN_TRANSACTION = {
    'bank_account': {
        'routing_number': '322271627',
        'account_number': '00987467838473',
        'name_on_account': 'Rob Otron',
    }
}

CUSTOMER = {
    'credit_card': CREDIT_CARD
}

REFUND_TRANSACTION = {
    'amount': 2222.00,
    'transaction_id': '2197513033',
    'last_four': '1111',
}


@attr('live_tests')
class TransactionTests(TestCase):

    def test_live_cim_sale_transaction(self):
        result = Customer.create(CUSTOMER)
        transaction = FULL_CARD_NOT_PRESENT_TRANSACTION.copy()
        transaction['customer_id'] = result.customer_id
        transaction['payment_id'] = result.payment_ids[0]

        # Create CIM sale transaction. If another sale is attempted too quickly,
        # an error will be thrown.
        transaction['amount'] = random.randrange(100, 100000) / 100.0
        result = Transaction.sale(transaction)
        self.assertRaises(AuthorizeResponseError, Transaction.sale, transaction)
        # Read transaction details
        Transaction.details(result.transaction_response.trans_id)

    def test_live_card_not_present_aim_sale_transaction(self):
        # Create AIM sale transaction
        transaction = FULL_CARD_NOT_PRESENT_TRANSACTION.copy()
        transaction['amount'] = random.randrange(100, 100000) / 100.0
        result = Transaction.sale(transaction)
        # Read transaction details
        Transaction.details(result.transaction_response.trans_id)

    def test_live_card_present_aim_sale_transaction(self):
        # Create AIM sale transaction
        transaction = FULL_CARD_PRESENT_TRANSACTION.copy()
        transaction['amount'] = random.randrange(100, 100000) / 100.0
        result = Transaction.sale(transaction)
        # Read transaction details
        Transaction.details(result.transaction_response.trans_id)

    def test_live_cim_auth_transaction(self):
        result = Customer.create(CUSTOMER)
        transaction = FULL_CIM_TRANSACTION.copy()
        transaction['customer_id'] = result.customer_id
        transaction['payment_id'] = result.payment_ids[0]
        transaction['amount'] = random.randrange(100, 100000) / 100.0
        result = Transaction.auth(transaction)
        # Read transaction details
        result = Transaction.details(result.transaction_response.trans_id)
        self.assertEqual(result.transaction.order.order_number, 'PONUM00001')

    def test_auth_and_settle_transaction(self):
        transaction = FULL_CARD_NOT_PRESENT_TRANSACTION.copy()
        transaction['amount'] = random.randrange(100, 100000) / 100.0
        result = Transaction.auth(transaction)
        Transaction.settle(result.transaction_response.trans_id)

    def test_credit(self):
        result = Customer.create(CUSTOMER)
        credit = {
            'amount': 40.00
        }
        credit['customer_id'] = result.customer_id
        credit['payment_id'] = result.payment_ids[0]
        Transaction.credit(credit)

    def test_refund_transaction(self):
        # Refunds will only work with settled transactions. We don't have a
        # settled transaction and so will check the exception that's thrown
        transaction = FULL_CARD_NOT_PRESENT_TRANSACTION.copy()
        transaction['amount'] = random.randrange(100, 100000) / 100.0
        result = Transaction.auth(transaction)
        self.assertRaises(AuthorizeResponseError, Transaction.refund, REFUND_TRANSACTION)

    def test_void_transaction(self):
        transaction = FULL_CARD_NOT_PRESENT_TRANSACTION.copy()
        transaction['amount'] = random.randrange(100, 100000) / 100.0
        result = Transaction.sale(transaction)
        Transaction.void(result.transaction_response.trans_id)

    def test_transaction_details(self):
        transaction = FULL_CARD_NOT_PRESENT_TRANSACTION.copy()
        transaction['amount'] = random.randrange(100, 100000) / 100.0
        result = Transaction.sale(transaction)
        Transaction.details(result.transaction_response.trans_id)

    def test_transaction_response_error_handling(self):
        # Issue 21: Hanlde transaction response errors which are different 
        # transaction errors. By running a bank account transaction over 
        # $200, we can replicate this strange processing behavior.
        transaction = BANK_ACCOUN_TRANSACTION.copy()
        transaction['amount'] = random.randrange(2001, 100000) / 100.0
        self.assertRaises(AuthorizeResponseError, Transaction.sale, transaction)

    def test_list_unsettled_transactions(self):
        Transaction.list()

    def test_list_transactions_by_batch(self):
        self.assertRaises(AuthorizeResponseError, Transaction.list, 'Bad batch ID')
