from authorize import Configuration
from authorize.xml_data import prettify

from unittest import TestCase

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

CREATE_ADDRESS_REQUEST = '''
<?xml version="1.0" ?>
<createCustomerShippingAddressRequest xmlns="AnetApi/xml/v1/schema/AnetApiSchema.xsd">
  <merchantAuthentication>
    <name>8s8tVnG5t</name>
    <transactionKey>5GK7mncw8mG2946z</transactionKey>
  </merchantAuthentication>
  <customerProfileId>1234567890</customerProfileId>
  <address>
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
  </address>
</createCustomerShippingAddressRequest>'''

DETAILS_ADDRESS_REQUEST = '''
<?xml version="1.0" ?>
<getCustomerShippingAddressRequest xmlns="AnetApi/xml/v1/schema/AnetApiSchema.xsd">
  <merchantAuthentication>
    <name>8s8tVnG5t</name>
    <transactionKey>5GK7mncw8mG2946z</transactionKey>
  </merchantAuthentication>
  <customerProfileId>1234567890</customerProfileId>
  <customerAddressId>0987654321</customerAddressId>
</getCustomerShippingAddressRequest>'''

UPDATE_ADDRESS_REQUEST = '''
<?xml version="1.0" ?>
<updateCustomerShippingAddressRequest xmlns="AnetApi/xml/v1/schema/AnetApiSchema.xsd">
  <merchantAuthentication>
    <name>8s8tVnG5t</name>
    <transactionKey>5GK7mncw8mG2946z</transactionKey>
  </merchantAuthentication>
  <customerProfileId>1234567890</customerProfileId>
  <address>
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
    <customerAddressId>0987654321</customerAddressId>
  </address>
</updateCustomerShippingAddressRequest>'''

DELETE_ADDRESS_REQUEST = '''
<?xml version="1.0" ?>
<deleteCustomerShippingAddressRequest xmlns="AnetApi/xml/v1/schema/AnetApiSchema.xsd">
  <merchantAuthentication>
    <name>8s8tVnG5t</name>
    <transactionKey>5GK7mncw8mG2946z</transactionKey>
  </merchantAuthentication>
  <customerProfileId>1234567890</customerProfileId>
  <customerAddressId>0987654321</customerAddressId>
</deleteCustomerShippingAddressRequest>'''


class AddressAPITests(TestCase):

    maxDiff = None

    def test_create_address_request(self):
        request_xml = Configuration.api.address._create_request('1234567890', ADDRESS)
        request_string = prettify(request_xml)
        self.assertEqual(request_string, CREATE_ADDRESS_REQUEST.strip())

    def test_details_address_request(self):
        request_xml = Configuration.api.address._details_request('1234567890', '0987654321')
        request_string = prettify(request_xml)
        self.assertEqual(request_string, DETAILS_ADDRESS_REQUEST.strip())

    def test_update_address_request(self):
        request_xml = Configuration.api.address._update_request('1234567890', '0987654321', ADDRESS)
        request_string = prettify(request_xml)
        self.assertEqual(request_string, UPDATE_ADDRESS_REQUEST.strip())

    def test_delete_address_request(self):
        request_xml = Configuration.api.address._delete_request('1234567890', '0987654321')
        request_string = prettify(request_xml)
        self.assertEqual(request_string, DELETE_ADDRESS_REQUEST.strip())
