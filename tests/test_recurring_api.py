from authorize import Configuration
from authorize.xml_data import prettify

from datetime import date

from unittest import TestCase


CREATE_RECURRING = {
    'name': 'Ultimate Robot Supreme Plan',
    'amount': 40.00,
    'total_occurrences': 30,
    'start_date': date.today().isoformat(),
    'interval_length': 2,
    'interval_unit': 'months',
    'trial_amount': 30.00,
    'trial_occurrences': 2,
    'credit_card': {
        'card_number': '4111111111111111',
        'expiration_month': '04',
        'expiration_year': '2014',
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
    'order': {
        'invoice_number': 'INV0001',
        'description': 'Just another invoice...',
    },
    'customer': {
        'merchant_id': '1234567890',
        'email': 'rob@robotronstudios.com',
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

UPDATE_RECURRING = {
    'name': 'Ultimate Robot Supreme Plan',
    'amount': 40.00,
    'total_occurrences': 30,
    'start_date': date.today().isoformat(),
    'trial_amount': 30.00,
    'trial_occurrences': 2,
    'credit_card': {
        'card_number': '4111111111111111',
        'expiration_month': '04',
        'expiration_year': '2014',
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
    'order': {
        'invoice_number': 'INV0001',
        'description': 'Just another invoice...',
    },
    'customer': {
        'merchant_id': '1234567890',
        'email': 'rob@robotronstudios.com',
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

UPDATE_RECURRING_NO_PAYMENT = UPDATE_RECURRING.copy()
del UPDATE_RECURRING_NO_PAYMENT['credit_card']

UPDATE_RECURRING_PAYMENT_ONLY = {
    'credit_card': {
        'card_number': '4111111111111111',
        'expiration_month': '04',
        'expiration_year': '2014',
        'card_code': '456',
    },
}

CREATE_RECURRING_REQUEST = '''
<?xml version="1.0" ?>
<ARBCreateSubscriptionRequest xmlns="AnetApi/xml/v1/schema/AnetApiSchema.xsd">
  <merchantAuthentication>
    <name>8s8tVnG5t</name>
    <transactionKey>5GK7mncw8mG2946z</transactionKey>
  </merchantAuthentication>
  <subscription>
    <name>Ultimate Robot Supreme Plan</name>
    <paymentSchedule>
      <interval>
        <length>2</length>
        <unit>months</unit>
      </interval>
      <startDate>{0}</startDate>
      <totalOccurrences>30</totalOccurrences>
      <trialOccurrences>2</trialOccurrences>
    </paymentSchedule>
    <amount>40.00</amount>
    <trialAmount>30.00</trialAmount>
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
    <customer>
      <id>1234567890</id>
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
    </shipTo>
  </subscription>
</ARBCreateSubscriptionRequest>
'''.format(date.today().isoformat())

DETAILS_RECURRING_REQUEST = '''
<?xml version="1.0" ?>
<ARBGetSubscriptionStatusRequest xmlns="AnetApi/xml/v1/schema/AnetApiSchema.xsd">
  <merchantAuthentication>
    <name>8s8tVnG5t</name>
    <transactionKey>5GK7mncw8mG2946z</transactionKey>
  </merchantAuthentication>
  <subscriptionId>0932576929034</subscriptionId>
</ARBGetSubscriptionStatusRequest>
'''

UPDATE_RECURRING_REQUEST = '''
<?xml version="1.0" ?>
<ARBUpdateSubscriptionRequest xmlns="AnetApi/xml/v1/schema/AnetApiSchema.xsd">
  <merchantAuthentication>
    <name>8s8tVnG5t</name>
    <transactionKey>5GK7mncw8mG2946z</transactionKey>
  </merchantAuthentication>
  <subscriptionId>0932576929034</subscriptionId>
  <subscription>
    <name>Ultimate Robot Supreme Plan</name>
    <paymentSchedule>
      <startDate>{0}</startDate>
      <totalOccurrences>30</totalOccurrences>
      <trialOccurrences>2</trialOccurrences>
    </paymentSchedule>
    <amount>40.00</amount>
    <trialAmount>30.00</trialAmount>
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
    <customer>
      <id>1234567890</id>
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
    </shipTo>
  </subscription>
</ARBUpdateSubscriptionRequest>
'''.format(date.today().isoformat())

UPDATE_RECURRING_NO_PAYMENT_REQUEST = '''
<?xml version="1.0" ?>
<ARBUpdateSubscriptionRequest xmlns="AnetApi/xml/v1/schema/AnetApiSchema.xsd">
  <merchantAuthentication>
    <name>8s8tVnG5t</name>
    <transactionKey>5GK7mncw8mG2946z</transactionKey>
  </merchantAuthentication>
  <subscriptionId>0932576929034</subscriptionId>
  <subscription>
    <name>Ultimate Robot Supreme Plan</name>
    <paymentSchedule>
      <startDate>{0}</startDate>
      <totalOccurrences>30</totalOccurrences>
      <trialOccurrences>2</trialOccurrences>
    </paymentSchedule>
    <amount>40.00</amount>
    <trialAmount>30.00</trialAmount>
    <order>
      <invoiceNumber>INV0001</invoiceNumber>
      <description>Just another invoice...</description>
    </order>
    <customer>
      <id>1234567890</id>
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
    </shipTo>
  </subscription>
</ARBUpdateSubscriptionRequest>
'''.format(date.today().isoformat())

UPDATE_RECURRING_PAYMENT_ONLY_REQUEST = '''
<?xml version="1.0" ?>
<ARBUpdateSubscriptionRequest xmlns="AnetApi/xml/v1/schema/AnetApiSchema.xsd">
  <merchantAuthentication>
    <name>8s8tVnG5t</name>
    <transactionKey>5GK7mncw8mG2946z</transactionKey>
  </merchantAuthentication>
  <subscriptionId>0932576929034</subscriptionId>
  <subscription>
    <paymentSchedule/>
    <payment>
      <creditCard>
        <cardNumber>4111111111111111</cardNumber>
        <expirationDate>2014-04</expirationDate>
        <cardCode>456</cardCode>
      </creditCard>
    </payment>
  </subscription>
</ARBUpdateSubscriptionRequest>
'''

DELETE_RECURRING_REQUEST = '''
<?xml version="1.0" ?>
<ARBCancelSubscriptionRequest xmlns="AnetApi/xml/v1/schema/AnetApiSchema.xsd">
  <merchantAuthentication>
    <name>8s8tVnG5t</name>
    <transactionKey>5GK7mncw8mG2946z</transactionKey>
  </merchantAuthentication>
  <subscriptionId>0932576929034</subscriptionId>
</ARBCancelSubscriptionRequest>
'''


class RecurringAPITests(TestCase):

    maxDiff = None

    def test_create_recurring_request(self):
        request_xml = Configuration.api.recurring._create_request(CREATE_RECURRING)
        request_string = prettify(request_xml)
        self.assertEqual(request_string, CREATE_RECURRING_REQUEST.strip())

    def test_details_recurring_request(self):
        request_xml = Configuration.api.recurring._details_request('0932576929034')
        request_string = prettify(request_xml)
        self.assertEqual(request_string, DETAILS_RECURRING_REQUEST.strip())

    def test_update_recurring_request(self):
        request_xml = Configuration.api.recurring._update_request('0932576929034', UPDATE_RECURRING)
        request_string = prettify(request_xml)
        self.assertEqual(request_string, UPDATE_RECURRING_REQUEST.strip())

        request_xml = Configuration.api.recurring._update_request('0932576929034', UPDATE_RECURRING_PAYMENT_ONLY)
        request_string = prettify(request_xml)
        self.assertEqual(request_string, UPDATE_RECURRING_PAYMENT_ONLY_REQUEST.strip())

        request_xml = Configuration.api.recurring._update_request('0932576929034', UPDATE_RECURRING_NO_PAYMENT)
        request_string = prettify(request_xml)
        self.assertEqual(request_string, UPDATE_RECURRING_NO_PAYMENT_REQUEST.strip())

    def test_delete_recurring_request(self):
        request_xml = Configuration.api.recurring._delete_request('0932576929034')
        request_string = prettify(request_xml)
        self.assertEqual(request_string, DELETE_RECURRING_REQUEST.strip())
