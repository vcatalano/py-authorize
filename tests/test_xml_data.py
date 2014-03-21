from authorize.xml_data import *
from unittest import TestCase

PROFILE = {
    'merchant_id': '1234567890',
    'email': 'rob@robotronstudios.com',
    'description': 'I am a robot',
}

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

CREDIT_CARD = {
    'card_number': '4111111111111111',
    'expiration_year': '2014',
    'expiration_month': '04',
    'card_code': '343',
}

BANK_ACCOUNT = {
    'account_type': 'checking',
    'routing_number': '322271627',
    'account_number': '00987467838473',
    'name_on_account': 'Rob Otron',
    'bank_name': 'Evil Bank Co.',
    'echeck_type': 'WEB',
}

LINE_ITEM = {
    'item_id': 'CIR0001',
    'name': 'Circuit Board',
    'description': 'A brand new robot component',
    'quantity': 5,
    'unit_price': 99.99,
    'taxable': True,
}

LINE_ITEMS = [{
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
    'taxable': False,
}]

TAX_AMOUNT_TYPE = {
    'amount': 45.00,
    'name': 'Double Taxation Tax',
    'description': 'Another tax for paying double tax',
}

ORDER = {
    'invoice_number': 'INV0001',
    'description': 'Just another invoice...',
}

CREATE_PROFILE_XML = '''
<?xml version="1.0" ?>
<profile>
  <merchantCustomerId>1234567890</merchantCustomerId>
  <description>I am a robot</description>
  <email>rob@robotronstudios.com</email>
</profile>
'''

CREATE_ADDRESS_XML = '''
<?xml version="1.0" ?>
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
'''

CREATE_CARD_XML = '''
<?xml version="1.0" ?>
<creditCard>
  <cardNumber>4111111111111111</cardNumber>
  <expirationDate>2014-04</expirationDate>
  <cardCode>343</cardCode>
</creditCard>
'''

CREATE_ACCOUNT_XML = '''
<?xml version="1.0" ?>
<bankAccount>
  <accountType>checking</accountType>
  <routingNumber>322271627</routingNumber>
  <accountNumber>00987467838473</accountNumber>
  <nameOnAccount>Rob Otron</nameOnAccount>
  <echeckType>WEB</echeckType>
  <bankName>Evil Bank Co.</bankName>
</bankAccount>
'''

CREATE_LINE_ITEM_XML = '''
<?xml version="1.0" ?>
<lineItem>
  <itemId>CIR0001</itemId>
  <name>Circuit Board</name>
  <description>A brand new robot component</description>
  <quantity>5</quantity>
  <unitPrice>99.99</unitPrice>
  <taxable>true</taxable>
</lineItem>
'''

CREATE_LINE_ITEMS_XML = '''
<?xml version="1.0" ?>
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
    <taxable>false</taxable>
  </lineItem>
</lineItems>
'''

CREATE_AMOUNT_TYPE_XML = '''
<?xml version="1.0" ?>
<tax>
  <amount>45.00</amount>
  <name>Double Taxation Tax</name>
  <description>Another tax for paying double tax</description>
</tax>
'''

CREATE_ORDER_XML = '''
<?xml version="1.0" ?>
<order>
  <invoiceNumber>INV0001</invoiceNumber>
  <description>Just another invoice...</description>
</order>
'''


class XMLDataTests(TestCase):

    maxDiff = None

    def test_create_profile(self):
        profile_xml = create_profile(PROFILE)
        profile_string = prettify(profile_xml)
        self.assertEqual(profile_string, CREATE_PROFILE_XML.strip())

    def test_create_address(self):
        address_xml = create_address('billTo', ADDRESS)
        address_string = prettify(address_xml)
        self.assertEqual(address_string, CREATE_ADDRESS_XML.strip())

    def test_create_card(self):
        card_xml = create_card(CREDIT_CARD)
        card_string = prettify(card_xml)
        self.assertEqual(card_string, CREATE_CARD_XML.strip())

    def test_create_account(self):
        account_xml = create_account(BANK_ACCOUNT)
        account_string = prettify(account_xml)
        self.assertEqual(account_string, CREATE_ACCOUNT_XML.strip())

    def test_create_line_item(self):
        line_item_xml = create_line_item('lineItem', LINE_ITEM)
        line_item_string = prettify(line_item_xml)
        self.assertEqual(line_item_string, CREATE_LINE_ITEM_XML.strip())

    def test_create_line_items(self):
        line_items_xml = create_line_items(LINE_ITEMS)
        line_items_string = prettify(line_items_xml)
        self.assertEqual(line_items_string, CREATE_LINE_ITEMS_XML.strip())

    def test_create_amount_type(self):
        tax_amount_type_xml = create_amount_type('tax', TAX_AMOUNT_TYPE)
        tax_amount_type_string = prettify(tax_amount_type_xml)
        self.assertEqual(tax_amount_type_string, CREATE_AMOUNT_TYPE_XML.strip())

    def test_create_order(self):
        order_xml = create_order(ORDER)
        order_string = prettify(order_xml)
        self.assertEqual(order_string, CREATE_ORDER_XML.strip())
