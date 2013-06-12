import xml.etree.cElementTree as E

from authorize.apis.base_api import BaseAPI
from authorize.xml_data import *


class PaymentProfileAPI(BaseAPI):

    def details(self, customer_id, payment_id):
        return self.api._make_call(self._details_request(customer_id, payment_id))

    def delete(self, customer_id, payment_id):
        self.api._make_call(self._delete_request(customer_id, payment_id))

    # The following methods generate the XML for the corresponding API calls.
    # This makes unit testing each of the calls easier.
    def _details_request(self, customer_id, payment_id):
        request = self.api._base_request('getCustomerPaymentProfileRequest')
        E.SubElement(request, 'customerProfileId').text = customer_id
        E.SubElement(request, 'customerPaymentProfileId').text = payment_id
        return request

    def _delete_request(self, customer_id, payment_id):
        request = self.api._base_request('deleteCustomerPaymentProfileRequest')
        E.SubElement(request, 'customerProfileId').text = customer_id
        E.SubElement(request, 'customerPaymentProfileId').text = payment_id
        return request

    def _make_xml(self, method, customer_id=None, payment_id=None, params={}):
        request = self.api._base_request(method)

        if customer_id:
            E.SubElement(request, 'customerProfileId').text = customer_id

        profile = E.Element('paymentProfile')

        if 'customer_type' in params:
            E.SubElement(profile, 'customerType').text = params['customer_type']

        if 'billing' in params:
            profile.append(create_address('billTo', params['billing']))

        profile.append(create_payment(params))
        request.append(profile)

        if payment_id:
            E.SubElement(profile, 'customerPaymentProfileId').text = payment_id

        return request
