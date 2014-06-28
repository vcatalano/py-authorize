from authorize import Configuration
from authorize.xml_data import prettify

from unittest import TestCase

FULL_CIM_TRANSACTION = {
    'amount': 30.00,
    'customer_id': '1234567890',
    'payment_id': '0987654321',
    'address_id': '93832984',
    'credit_card': {
        'card_number': '4111111111111111',
        'card_code': '456',
        'expiration_month': '04',
        'expiration_year': '2014',
    },
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
        'customer_ip': '100.0.0.1',
    },
    'tax_exempt': False,
    'recurring': True,
    'card_code': '443',
}

FULL_CARD_NOT_PRESENT_AIM_TRANSACTION = {
    'amount': 30.00,
    'email': 'rob@robotronstudios.com',
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

FULL_CARD_PRESENT_AIM_TRANSACTION = {
    'amount': 30.00,
    'email': 'rob@robotronstudios.com',
    'track_data': {
        'track_1': "B4111111111111111^OTERON/ROB^1401101",
        'track_2': "4111111111111111=1401101",
    },
    'retail': {
        'market_type': 2,
        'device_type': 1,
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

REFUND_TRANSACTION = {
    'amount': 112.00,
    'transaction_id': '87912412523',
    'last_four': '1111',
}

CIM_SALE_REQUEST = '''
<?xml version="1.0" ?>
<createCustomerProfileTransactionRequest xmlns="AnetApi/xml/v1/schema/AnetApiSchema.xsd">
  <merchantAuthentication>
    <name>8s8tVnG5t</name>
    <transactionKey>5GK7mncw8mG2946z</transactionKey>
  </merchantAuthentication>
  <transaction>
    <profileTransAuthCapture>
      <amount>30.00</amount>
      <tax>
        <amount>45.00</amount>
        <name>Double Taxation Tax</name>
        <description>Another tax for paying double tax</description>
      </tax>
      <shipping>
        <amount>10.00</amount>
        <name>UPS 2-Day Shipping</name>
        <description>Handle with care</description>
      </shipping>
      <duty>
        <amount>90.00</amount>
        <name>The amount for duty</name>
        <description>I cant believe you would pay for duty</description>
      </duty>
      <lineItems>
        <itemId>CIR0001</itemId>
        <name>Circuit Board</name>
        <description>A brand new robot component</description>
        <quantity>5</quantity>
        <unitPrice>99.99</unitPrice>
        <taxable>true</taxable>
      </lineItems>
      <lineItems>
        <itemId>CIR0002</itemId>
        <name>Circuit Board 2.0</name>
        <description>Another new robot component</description>
        <quantity>1</quantity>
        <unitPrice>86.99</unitPrice>
        <taxable>true</taxable>
      </lineItems>
      <lineItems>
        <itemId>SCRDRVR</itemId>
        <name>Screwdriver</name>
        <description>A basic screwdriver</description>
        <quantity>1</quantity>
        <unitPrice>10.00</unitPrice>
        <taxable>true</taxable>
      </lineItems>
      <customerProfileId>1234567890</customerProfileId>
      <customerPaymentProfileId>0987654321</customerPaymentProfileId>
      <customerShippingAddressId>93832984</customerShippingAddressId>
      <order>
        <invoiceNumber>INV0001</invoiceNumber>
        <description>Just another invoice...</description>
        <purchaseOrderNumber>PONUM00001</purchaseOrderNumber>
      </order>
      <taxExempt>false</taxExempt>
      <recurringBilling>true</recurringBilling>
    </profileTransAuthCapture>
  </transaction>
  <extraOptions>
<![CDATA[x_customer_ip=100.0.0.1]]>  </extraOptions>
</createCustomerProfileTransactionRequest>
'''

CARD_NOT_PRESENT_AIM_SALE_REQUEST = '''
<?xml version="1.0" ?>
<createTransactionRequest xmlns="AnetApi/xml/v1/schema/AnetApiSchema.xsd">
  <merchantAuthentication>
    <name>8s8tVnG5t</name>
    <transactionKey>5GK7mncw8mG2946z</transactionKey>
  </merchantAuthentication>
  <transactionRequest>
    <transactionType>authCaptureTransaction</transactionType>
    <amount>30.00</amount>
    <payment>
      <creditCard>
        <cardNumber>4111111111111111</cardNumber>
        <expirationDate>2014-04</expirationDate>
        <cardCode>456</cardCode>
      </creditCard>
    </payment>
    <order>
      <invoiceNumber>INV0001</invoiceNumber>
      <description>Just another invoice...</description>
    </order>
    <lineItems>
      <lineItem>
        <itemId>CIR0001</itemId>
        <name>Circuit Board</name>
        <description>A brand new robot component</description>
        <quantity>5</quantity>
        <unitPrice>99.99</unitPrice>
        <taxable>true</taxable>
      </lineItem>
      <lineItem>
        <itemId>CIR0002</itemId>
        <name>Circuit Board 2.0</name>
        <description>Another new robot component</description>
        <quantity>1</quantity>
        <unitPrice>86.99</unitPrice>
        <taxable>true</taxable>
      </lineItem>
      <lineItem>
        <itemId>SCRDRVR</itemId>
        <name>Screwdriver</name>
        <description>A basic screwdriver</description>
        <quantity>1</quantity>
        <unitPrice>10.00</unitPrice>
        <taxable>true</taxable>
      </lineItem>
    </lineItems>
    <tax>
      <amount>45.00</amount>
      <name>Double Taxation Tax</name>
      <description>Another tax for paying double tax</description>
    </tax>
    <duty>
      <amount>90.00</amount>
      <name>The amount for duty</name>
      <description>I cant believe you would pay for duty</description>
    </duty>
    <shipping>
      <amount>10.00</amount>
      <name>UPS 2-Day Shipping</name>
      <description>Handle with care</description>
    </shipping>
    <taxExempt>false</taxExempt>
    <customer>
      <email>rob@robotronstudios.com</email>
    </customer>
    <billTo>
      <firstName>Rob</firstName>
      <lastName>Oteron</lastName>
      <company>Robotron Studios</company>
      <address>101 Computer Street</address>
      <city>Tucson</city>
      <state>AZ</state>
      <zip>85704</zip>
      <country>US</country>
      <phoneNumber>520-123-4567</phoneNumber>
      <faxNumber>520-456-7890</faxNumber>
    </billTo>
    <shipTo>
      <firstName>Rob</firstName>
      <lastName>Oteron</lastName>
      <company>Robotron Studios</company>
      <address>101 Computer Street</address>
      <city>Tucson</city>
      <state>AZ</state>
      <zip>85704</zip>
      <country>US</country>
      <phoneNumber>520-123-4567</phoneNumber>
      <faxNumber>520-456-7890</faxNumber>
    </shipTo>
    <customerIP>100.0.0.1</customerIP>
  </transactionRequest>
</createTransactionRequest>
'''

CARD_PRESENT_AIM_SALE_REQUEST = '''
<?xml version="1.0" ?>
<createTransactionRequest xmlns="AnetApi/xml/v1/schema/AnetApiSchema.xsd">
  <merchantAuthentication>
    <name>8s8tVnG5t</name>
    <transactionKey>5GK7mncw8mG2946z</transactionKey>
  </merchantAuthentication>
  <transactionRequest>
    <transactionType>authCaptureTransaction</transactionType>
    <amount>30.00</amount>
    <payment>
      <trackData>
        <track1>B4111111111111111^OTERON/ROB^1401101</track1>
        <track2>4111111111111111=1401101</track2>
      </trackData>
    </payment>
    <order>
      <invoiceNumber>INV0001</invoiceNumber>
      <description>Just another invoice...</description>
    </order>
    <lineItems>
      <lineItem>
        <itemId>CIR0001</itemId>
        <name>Circuit Board</name>
        <description>A brand new robot component</description>
        <quantity>5</quantity>
        <unitPrice>99.99</unitPrice>
        <taxable>true</taxable>
      </lineItem>
      <lineItem>
        <itemId>CIR0002</itemId>
        <name>Circuit Board 2.0</name>
        <description>Another new robot component</description>
        <quantity>1</quantity>
        <unitPrice>86.99</unitPrice>
        <taxable>true</taxable>
      </lineItem>
      <lineItem>
        <itemId>SCRDRVR</itemId>
        <name>Screwdriver</name>
        <description>A basic screwdriver</description>
        <quantity>1</quantity>
        <unitPrice>10.00</unitPrice>
        <taxable>true</taxable>
      </lineItem>
    </lineItems>
    <tax>
      <amount>45.00</amount>
      <name>Double Taxation Tax</name>
      <description>Another tax for paying double tax</description>
    </tax>
    <duty>
      <amount>90.00</amount>
      <name>The amount for duty</name>
      <description>I cant believe you would pay for duty</description>
    </duty>
    <shipping>
      <amount>10.00</amount>
      <name>UPS 2-Day Shipping</name>
      <description>Handle with care</description>
    </shipping>
    <taxExempt>false</taxExempt>
    <customer>
      <email>rob@robotronstudios.com</email>
    </customer>
    <billTo>
      <firstName>Rob</firstName>
      <lastName>Oteron</lastName>
      <company>Robotron Studios</company>
      <address>101 Computer Street</address>
      <city>Tucson</city>
      <state>AZ</state>
      <zip>85704</zip>
      <country>US</country>
      <phoneNumber>520-123-4567</phoneNumber>
      <faxNumber>520-456-7890</faxNumber>
    </billTo>
    <shipTo>
      <firstName>Rob</firstName>
      <lastName>Oteron</lastName>
      <company>Robotron Studios</company>
      <address>101 Computer Street</address>
      <city>Tucson</city>
      <state>AZ</state>
      <zip>85704</zip>
      <country>US</country>
      <phoneNumber>520-123-4567</phoneNumber>
      <faxNumber>520-456-7890</faxNumber>
    </shipTo>
    <customerIP>100.0.0.1</customerIP>
    <retail>
      <marketType>2</marketType>
      <deviceType>1</deviceType>
    </retail>
  </transactionRequest>
</createTransactionRequest>
'''

SETTLE_REQUEST = '''
<?xml version="1.0" ?>
<createTransactionRequest xmlns="AnetApi/xml/v1/schema/AnetApiSchema.xsd">
  <merchantAuthentication>
    <name>8s8tVnG5t</name>
    <transactionKey>5GK7mncw8mG2946z</transactionKey>
  </merchantAuthentication>
  <transactionRequest>
    <transactionType>priorAuthCaptureTransaction</transactionType>
    <refTransId>87912412523</refTransId>
  </transactionRequest>
</createTransactionRequest>
'''

REFUND_REQUEST = '''
<?xml version="1.0" ?>
<createTransactionRequest xmlns="AnetApi/xml/v1/schema/AnetApiSchema.xsd">
  <merchantAuthentication>
    <name>8s8tVnG5t</name>
    <transactionKey>5GK7mncw8mG2946z</transactionKey>
  </merchantAuthentication>
  <transactionRequest>
    <transactionType>refundTransaction</transactionType>
    <amount>112.00</amount>
    <payment>
      <creditCard>
        <cardNumber>1111</cardNumber>
        <expirationDate>XXXXXX</expirationDate>
      </creditCard>
    </payment>
    <refTransId>87912412523</refTransId>
  </transactionRequest>
</createTransactionRequest>
'''

VOID_REQUEST = '''
<?xml version="1.0" ?>
<createTransactionRequest xmlns="AnetApi/xml/v1/schema/AnetApiSchema.xsd">
  <merchantAuthentication>
    <name>8s8tVnG5t</name>
    <transactionKey>5GK7mncw8mG2946z</transactionKey>
  </merchantAuthentication>
  <transactionRequest>
    <transactionType>voidTransaction</transactionType>
    <refTransId>87912412523</refTransId>
  </transactionRequest>
</createTransactionRequest>
'''

DETAILS_REQUEST = '''
<?xml version="1.0" ?>
<getTransactionDetailsRequest xmlns="AnetApi/xml/v1/schema/AnetApiSchema.xsd">
  <merchantAuthentication>
    <name>8s8tVnG5t</name>
    <transactionKey>5GK7mncw8mG2946z</transactionKey>
  </merchantAuthentication>
  <transId>87912412523</transId>
</getTransactionDetailsRequest>
'''

UNSETTLED_LIST_REQUEST = '''
<?xml version="1.0" ?>
<getUnsettledTransactionListRequest xmlns="AnetApi/xml/v1/schema/AnetApiSchema.xsd">
  <merchantAuthentication>
    <name>8s8tVnG5t</name>
    <transactionKey>5GK7mncw8mG2946z</transactionKey>
  </merchantAuthentication>
</getUnsettledTransactionListRequest>
'''

SETTLED_LIST_REQUEST = '''
<?xml version="1.0" ?>
<getTransactionListRequest xmlns="AnetApi/xml/v1/schema/AnetApiSchema.xsd">
  <merchantAuthentication>
    <name>8s8tVnG5t</name>
    <transactionKey>5GK7mncw8mG2946z</transactionKey>
  </merchantAuthentication>
  <batchId>89429992353</batchId>
</getTransactionListRequest>
'''


class TransactionAPITests(TestCase):

    maxDiff = None

    def test_cim_base_request(self):
        request_xml = Configuration.api.transaction._cim_base_request(
            'profileTransAuthCapture', FULL_CIM_TRANSACTION)
        request_string = prettify(request_xml)
        self.assertEqual(request_string, CIM_SALE_REQUEST.strip())

    def test_card_not_present_aim_base_request(self):
        request_xml = Configuration.api.transaction._aim_base_request(
            'authCaptureTransaction', FULL_CARD_NOT_PRESENT_AIM_TRANSACTION)
        request_string = prettify(request_xml)
        self.assertEqual(request_string, CARD_NOT_PRESENT_AIM_SALE_REQUEST.strip())

    def test_card_present_aim_base_request(self):
        request_xml = Configuration.api.transaction._aim_base_request(
            'authCaptureTransaction', FULL_CARD_PRESENT_AIM_TRANSACTION)
        request_string = prettify(request_xml)
        self.assertEqual(request_string, CARD_PRESENT_AIM_SALE_REQUEST.strip())

    def test_cim_auth_request(self):
        request_xml = Configuration.api.transaction._cim_base_request(
            'profileTransAuthOnly', FULL_CIM_TRANSACTION)
        request_string = prettify(request_xml)
        self.assertEqual(request_string, CIM_SALE_REQUEST.strip()
            .replace('AuthCapture', 'AuthOnly'))

    def test_settle_request(self):
        request_xml = Configuration.api.transaction._settle_request(
            '87912412523')
        request_string = prettify(request_xml)
        self.assertEqual(request_string, SETTLE_REQUEST.strip())

    def test_refund_request(self):
        request_xml = Configuration.api.transaction._refund_request(
            REFUND_TRANSACTION)
        request_string = prettify(request_xml)
        self.assertEqual(request_string, REFUND_REQUEST.strip())

    def test_void_request(self):
        request_xml = Configuration.api.transaction._void_request(
            '87912412523')
        request_string = prettify(request_xml)
        self.assertEqual(request_string, VOID_REQUEST.strip())

    def test_details_request(self):
        request_xml = Configuration.api.transaction._details_request(
            '87912412523')
        request_string = prettify(request_xml)
        self.assertEqual(request_string, DETAILS_REQUEST.strip())

    def test_unsettled_list_request(self):
        request_xml = Configuration.api.transaction._unsettled_list_request()
        request_string = prettify(request_xml)
        self.assertEqual(request_string, UNSETTLED_LIST_REQUEST.strip())

    def test_settled_list_request(self):
        request_xml = Configuration.api.transaction._settled_list_request(
            '89429992353')
        request_string = prettify(request_xml)
        self.assertEqual(request_string, SETTLED_LIST_REQUEST.strip())
