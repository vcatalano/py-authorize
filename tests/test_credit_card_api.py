from authorize.configuration import Configuration
from authorize.xml_data import prettify

from unittest import TestCase

CREDIT_CARD = {
    'customer_type': 'individual',
    'card_number': '4111111111111111',
    'card_code': '456',
    'expiration_month': '04',
    'expiration_year': '2014',
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

VALIDATE_CREDIT_CARD = {
    'address_id': '7982053235',
    'card_code': '456',
    'validation_mode': 'testMode',
}

CREATE_CREDIT_CARD_REQUEST = '''
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
      <creditCard>
        <cardNumber>4111111111111111</cardNumber>
        <expirationDate>2014-04</expirationDate>
        <cardCode>456</cardCode>
      </creditCard>
    </payment>
  </paymentProfile>
</createCustomerPaymentProfileRequest>
'''

DETAILS_CREDIT_CARD_REQUEST = '''
<?xml version="1.0" ?>
<getCustomerPaymentProfileRequest xmlns="AnetApi/xml/v1/schema/AnetApiSchema.xsd">
  <merchantAuthentication>
    <name>8s8tVnG5t</name>
    <transactionKey>5GK7mncw8mG2946z</transactionKey>
  </merchantAuthentication>
  <customerProfileId>1234567890</customerProfileId>
  <customerPaymentProfileId>0987654321</customerPaymentProfileId>
</getCustomerPaymentProfileRequest>
'''

UPDATE_CREDIT_CARD_REQUEST = '''
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
      <creditCard>
        <cardNumber>4111111111111111</cardNumber>
        <expirationDate>2014-04</expirationDate>
        <cardCode>456</cardCode>
      </creditCard>
    </payment>
    <customerPaymentProfileId>0987654321</customerPaymentProfileId>
  </paymentProfile>
</updateCustomerPaymentProfileRequest>
'''

DELETE_CREDIT_CARD_REQUEST = '''
<?xml version="1.0" ?>
<deleteCustomerPaymentProfileRequest xmlns="AnetApi/xml/v1/schema/AnetApiSchema.xsd">
  <merchantAuthentication>
    <name>8s8tVnG5t</name>
    <transactionKey>5GK7mncw8mG2946z</transactionKey>
  </merchantAuthentication>
  <customerProfileId>1234567890</customerProfileId>
  <customerPaymentProfileId>0987654321</customerPaymentProfileId>
</deleteCustomerPaymentProfileRequest>
'''

VALIDATE_CREDIT_CARD_REQUEST = '''
<?xml version="1.0" ?>
<validateCustomerPaymentProfileRequest xmlns="AnetApi/xml/v1/schema/AnetApiSchema.xsd">
  <merchantAuthentication>
    <name>8s8tVnG5t</name>
    <transactionKey>5GK7mncw8mG2946z</transactionKey>
  </merchantAuthentication>
  <customerProfileId>1234567890</customerProfileId>
  <customerPaymentProfileId>0987654321</customerPaymentProfileId>
  <customerShippingAddressId>7982053235</customerShippingAddressId>
  <cardCode>456</cardCode>
  <validationMode>testMode</validationMode>
</validateCustomerPaymentProfileRequest>
'''


class CreditCardAPITests(TestCase):

    maxDiff = None

    def test_create_credit_card_request(self):
        request_xml = Configuration.api.credit_card._create_request('1234567890', CREDIT_CARD)
        request_string = prettify(request_xml)
        self.assertEqual(request_string, CREATE_CREDIT_CARD_REQUEST.strip())

    def test_details_credit_card_request(self):
        request_xml = Configuration.api.credit_card._details_request('1234567890', '0987654321')
        request_string = prettify(request_xml)
        self.assertEqual(request_string, DETAILS_CREDIT_CARD_REQUEST.strip())

    def test_update_credit_card_request(self):
        request_xml = Configuration.api.credit_card._update_request('1234567890', '0987654321', CREDIT_CARD)
        request_string = prettify(request_xml)
        self.assertEqual(request_string, UPDATE_CREDIT_CARD_REQUEST.strip())

    def test_delete_credit_card_request(self):
        request_xml = Configuration.api.credit_card._delete_request('1234567890', '0987654321')
        request_string = prettify(request_xml)
        self.assertEqual(request_string, DELETE_CREDIT_CARD_REQUEST.strip())

    def test_validate_credit_card_request(self):
        request_xml = Configuration.api.credit_card._validate_request('1234567890', '0987654321', VALIDATE_CREDIT_CARD)
        request_string = prettify(request_xml)
        self.assertEqual(request_string, VALIDATE_CREDIT_CARD_REQUEST.strip())
