from authorize.apis.payment_profile_api import PaymentProfileAPI
from authorize.schemas import CreateBankAccountSchema
from authorize.xml_data import *


class BankAccountAPI(PaymentProfileAPI):

    def create(self, customer_id, params={}):
        card = self._deserialize(CreateBankAccountSchema(), params)
        return self.api._make_call(self._create_request(customer_id, card))

    def update(self, customer_id, payment_id, params={}):
        card = self._deserialize(CreateBankAccountSchema(), params)
        return self.api._make_call(self._update_request(customer_id, payment_id, card))

    # The following methods generate the XML for the corresponding API calls.
    # This makes unit testing each of the calls easier.
    def _create_request(self, customer_id, card={}):
        return self._make_xml('createCustomerPaymentProfileRequest', customer_id, None, params=card)

    def _update_request(self, customer_id, payment_id, card={}):
        return self._make_xml('updateCustomerPaymentProfileRequest', customer_id, payment_id, params=card)
