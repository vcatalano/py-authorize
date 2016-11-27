import xml.etree.cElementTree as E

try:
    import urllib.request as urllib2
except:
    import urllib2

from authorize.apis.address_api import AddressAPI
from authorize.apis.credit_card_api import CreditCardAPI
from authorize.apis.customer_api import CustomerAPI
from authorize.apis.bank_account_api import BankAccountAPI
from authorize.apis.batch_api import BatchAPI
from authorize.apis.recurring_api import RecurringAPI
from authorize.apis.transaction_api import TransactionAPI
from authorize.exceptions import AuthorizeConnectionError
from authorize.exceptions import AuthorizeResponseError
from authorize.response_parser import parse_response
from authorize.xml_data import *

E.register_namespace('', 'AnetApi/xml/v1/schema/AnetApiSchema.xsd')


class AuthorizeAPI(object):

    def __init__(self, config):
        """Allow for multiple instances of the Authorize API."""
        self.config = config
        self.customer = CustomerAPI(self)
        self.credit_card = CreditCardAPI(self)
        self.bank_account = BankAccountAPI(self)
        self.address = AddressAPI(self)
        self.recurring = RecurringAPI(self)
        self.batch = BatchAPI(self)
        self.transaction = TransactionAPI(self)
        self._client_auth = None

    @property
    def client_auth(self):
        """Generate an XML element with client auth data populated."""
        if not self._client_auth:
            self._client_auth = E.Element('merchantAuthentication')
            E.SubElement(self._client_auth, 'name').text = self.config.login_id
            E.SubElement(self._client_auth, 'transactionKey').text = self.config.transaction_key
        return self._client_auth

    def _base_request(self, method):
        """Factory method for generating the base XML requests."""
        request = E.Element(method)
        request.set('xmlns', 'AnetApi/xml/v1/schema/AnetApiSchema.xsd')
        request.append(self.client_auth)
        return request

    def _make_call(self, call):
        """Make a call to the Authorize.net server with the XML."""
        try:
            request = urllib2.Request(self.config.environment, E.tostring(call))
            request.add_header('Content-Type', 'text/xml')
            response = urllib2.urlopen(request).read()
            response = E.fromstring(response)
            response_json = parse_response(response)
        except urllib2.HTTPError:
            raise AuthorizeConnectionError('Error processing XML request.')

        # Exception handling for transaction response errors.
        try:
            error = response_json.transaction_response.errors[0]
            raise AuthorizeResponseError(error.error_code, error.error_text, response_json)
        except (KeyError, AttributeError):  # Attempt to access transaction response errors
            pass

        # Throw an exception for invalid calls. This makes error handling easier.
        if response_json.messages[0].result_code != 'Ok':
            error = response_json.messages[0].message
            raise AuthorizeResponseError(error.code, error.text, response_json)

        return response_json
