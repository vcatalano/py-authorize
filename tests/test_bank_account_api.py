from authorize import Configuration
from authorize.xml_data import prettify

from unittest import TestCase

CREATE_BANK_ACCOUNT = {
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

UPDATE_BANK_ACCOUNT = {
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

CREATE_BANK_ACCOUNT_REQUEST = '''
<?xml version="1.0" ?>
<createCustomerPaymentProfileRequest xmlns="AnetApi/xml/v1/schema/AnetApiSchema.xsd">
  <merchantAuthentication>
    <name>8s8tVnG5t</name>
    <transactionKey>5GK7mncw8mG2946z</transactionKey>
  </merchantAuthentication>
  <customerProfileId>1234567890</customerProfileId>
  <paymentProfile>
    <customerType>individual</customerType>
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
    <payment>
      <bankAccount>
        <accountType>checking</accountType>
        <routingNumber>322271627</routingNumber>
        <accountNumber>00987467838473</accountNumber>
        <nameOnAccount>Rob Otron</nameOnAccount>
        <echeckType>CCD</echeckType>
        <bankName>Evil Bank Co.</bankName>
      </bankAccount>
    </payment>
  </paymentProfile>
</createCustomerPaymentProfileRequest>'''

DETAILS_BANK_ACCOUNT_REQUEST = '''
<?xml version="1.0" ?>
<getCustomerPaymentProfileRequest xmlns="AnetApi/xml/v1/schema/AnetApiSchema.xsd">
  <merchantAuthentication>
    <name>8s8tVnG5t</name>
    <transactionKey>5GK7mncw8mG2946z</transactionKey>
  </merchantAuthentication>
  <customerProfileId>1234567890</customerProfileId>
  <customerPaymentProfileId>0987654321</customerPaymentProfileId>
</getCustomerPaymentProfileRequest>'''

UPDATE_BANK_ACCOUNT_REQUEST = '''
<?xml version="1.0" ?>
<updateCustomerPaymentProfileRequest xmlns="AnetApi/xml/v1/schema/AnetApiSchema.xsd">
  <merchantAuthentication>
    <name>8s8tVnG5t</name>
    <transactionKey>5GK7mncw8mG2946z</transactionKey>
  </merchantAuthentication>
  <customerProfileId>1234567890</customerProfileId>
  <paymentProfile>
    <customerType>individual</customerType>
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
    <payment>
      <bankAccount>
        <accountType>checking</accountType>
        <routingNumber>322271627</routingNumber>
        <accountNumber>00987467838473</accountNumber>
        <nameOnAccount>Rob Otron</nameOnAccount>
        <echeckType>CCD</echeckType>
        <bankName>Evil Bank Co.</bankName>
      </bankAccount>
    </payment>
    <customerPaymentProfileId>0987654321</customerPaymentProfileId>
  </paymentProfile>
</updateCustomerPaymentProfileRequest>'''

DELETE_BANK_ACCOUNT_REQUEST = '''
<?xml version="1.0" ?>
<deleteCustomerPaymentProfileRequest xmlns="AnetApi/xml/v1/schema/AnetApiSchema.xsd">
  <merchantAuthentication>
    <name>8s8tVnG5t</name>
    <transactionKey>5GK7mncw8mG2946z</transactionKey>
  </merchantAuthentication>
  <customerProfileId>1234567890</customerProfileId>
  <customerPaymentProfileId>0987654321</customerPaymentProfileId>
</deleteCustomerPaymentProfileRequest>'''


class BankAccountAPITests(TestCase):

    maxDiff = None

    def test_create_bank_account_request(self):
        request_xml = Configuration.api.bank_account._create_request('1234567890', CREATE_BANK_ACCOUNT)
        request_string = prettify(request_xml)
        self.assertEqual(request_string, CREATE_BANK_ACCOUNT_REQUEST.strip())

    def test_details_bank_account_request(self):
        request_xml = Configuration.api.bank_account._details_request('1234567890', '0987654321')
        request_string = prettify(request_xml)
        self.assertEqual(request_string, DETAILS_BANK_ACCOUNT_REQUEST.strip())

    def test_update_bank_account_request(self):
        request_xml = Configuration.api.bank_account._update_request('1234567890', '0987654321', UPDATE_BANK_ACCOUNT)
        request_string = prettify(request_xml)
        self.assertEqual(request_string, UPDATE_BANK_ACCOUNT_REQUEST.strip())

    def test_delete_bank_account_request(self):
        request_xml = Configuration.api.bank_account._delete_request('1234567890', '0987654321')
        request_string = prettify(request_xml)
        self.assertEqual(request_string, DELETE_BANK_ACCOUNT_REQUEST.strip())
