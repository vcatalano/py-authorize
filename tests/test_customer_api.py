from authorize import Configuration
from authorize.xml_data import prettify

from unittest import TestCase


CREATE_CUSTOMER = {
    'merchant_id': '1234567890',
    'email': 'rob@robotronstudios.com',
    'description': 'I am a robot',
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
        'account_type': 'checking',
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
    },
}

UPDATE_CUSTOMER = {
    'merchant_id': '1234567890',
    'email': 'rob@robotronstudios.com',
    'description': 'I am a robot',
    'customer_type': 'individual',
}

CREATE_CUSTOMER_REQUEST = '''
<?xml version="1.0" ?>
<createCustomerProfileRequest xmlns="AnetApi/xml/v1/schema/AnetApiSchema.xsd">
  <merchantAuthentication>
    <name>8s8tVnG5t</name>
    <transactionKey>5GK7mncw8mG2946z</transactionKey>
  </merchantAuthentication>
  <profile>
    <merchantCustomerId>1234567890</merchantCustomerId>
    <description>I am a robot</description>
    <email>rob@robotronstudios.com</email>
    <paymentProfiles>
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
    </paymentProfiles>
    <shipToList>
      <firstName>Rob</firstName>
      <lastName>Oteron</lastName>
      <company>Robotron Studios</company>
      <address>101 Computer Street</address>
      <city>Tucson</city>
      <state>AZ</state>
      <zip>85704</zip>
      <country>US</country>
    </shipToList>
  </profile>
</createCustomerProfileRequest>
'''

CUSTOMER_DETAILS_REQUEST = '''
<?xml version="1.0" ?>
<getCustomerProfileRequest xmlns="AnetApi/xml/v1/schema/AnetApiSchema.xsd">
  <merchantAuthentication>
    <name>8s8tVnG5t</name>
    <transactionKey>5GK7mncw8mG2946z</transactionKey>
  </merchantAuthentication>
  <customerProfileId>1234567890</customerProfileId>
</getCustomerProfileRequest>
'''

CUSTOMER_UPDATE_REQUEST = '''
<?xml version="1.0" ?>
<updateCustomerProfileRequest xmlns="AnetApi/xml/v1/schema/AnetApiSchema.xsd">
  <merchantAuthentication>
    <name>8s8tVnG5t</name>
    <transactionKey>5GK7mncw8mG2946z</transactionKey>
  </merchantAuthentication>
  <profile>
    <merchantCustomerId>1234567890</merchantCustomerId>
    <description>I am a robot</description>
    <email>rob@robotronstudios.com</email>
    <customerProfileId>1234567890</customerProfileId>
  </profile>
</updateCustomerProfileRequest>
'''

CUSTOMER_DELETE_REQUEST = '''
<?xml version="1.0" ?>
<deleteCustomerProfileRequest xmlns="AnetApi/xml/v1/schema/AnetApiSchema.xsd">
  <merchantAuthentication>
    <name>8s8tVnG5t</name>
    <transactionKey>5GK7mncw8mG2946z</transactionKey>
  </merchantAuthentication>
  <customerProfileId>1234567890</customerProfileId>
</deleteCustomerProfileRequest>
'''


class CustomerAPITests(TestCase):

    maxDiff = None

    def test_create_customer_request(self):
        request_xml = Configuration.api.customer._create_request(CREATE_CUSTOMER)
        request_string = prettify(request_xml)
        self.assertEqual(request_string, CREATE_CUSTOMER_REQUEST.strip())

    def test_details_customer_request(self):
        request_xml = Configuration.api.customer._details_request('1234567890')
        request_string = prettify(request_xml)
        self.assertEqual(request_string, CUSTOMER_DETAILS_REQUEST.strip())

    def test_update_customer_request(self):
        request_xml = Configuration.api.customer._update_request('1234567890', UPDATE_CUSTOMER)
        request_string = prettify(request_xml)
        self.assertEqual(request_string, CUSTOMER_UPDATE_REQUEST.strip())

    def test_delete_customer_request(self):
        request_xml = Configuration.api.customer._delete_request('1234567890')
        request_string = prettify(request_xml)
        self.assertEqual(request_string, CUSTOMER_DELETE_REQUEST.strip())
