import xml.etree.cElementTree as E

from authorize.apis.base_api import BaseAPI
from authorize.schemas import CustomerBaseSchema
from authorize.schemas import CreateCustomerSchema
from authorize.xml_data import *


class CustomerAPI(BaseAPI):

    def create(self, params={}):
        customer = self._deserialize(CreateCustomerSchema().bind(), params)
        return self.api._make_call(self._create_request(customer))

    def details(self, customer_id):
        return self.api._make_call(self._details_request(customer_id))

    def update(self, customer_id, params={}):
        customer = self._deserialize(CustomerBaseSchema().bind(), params)
        return self.api._make_call(self._update_request(customer_id, customer))

    def delete(self, customer_id):
        return self.api._make_call(self._delete_request(customer_id))

    def list(self):
        return self.api._make_call(self.api._base_request('getCustomerProfileIdsRequest'))

    # The following methods generate the XML for the corresponding API calls.
    # This makes unit testing each of the calls easier.
    def _create_request(self, customer={}):
        request = self.api._base_request('createCustomerProfileRequest')
        profile = create_profile(customer)

        payment_profiles = E.Element('paymentProfiles')

        # We are only concerned about payment profile information if a
        # payment method is included
        if 'credit_card' in customer or 'bank_account' in customer:
            # Customer type
            if 'customer_type' in customer:
                E.SubElement(payment_profiles, 'customerType').text = customer['customer_type']

            # Customer billing information
            if 'billing' in customer:
                payment_profiles.append(create_address('billTo', customer['billing']))

            # Payment method
            payment = E.SubElement(payment_profiles, 'payment')
            if 'credit_card' in customer:
                payment.append(create_card(customer['credit_card']))
            else:
                payment.append(create_account(customer['bank_account']))
            profile.append(payment_profiles)

        # Customer shipping information
        if 'shipping' in customer:
            profile.append(create_address('shipToList', customer['shipping']))

        request.append(profile)

        return request

    def _details_request(self, customer_id):
        request = self.api._base_request('getCustomerProfileRequest')
        E.SubElement(request, 'customerProfileId').text = customer_id
        return request

    def _update_request(self, customer_id, customer):
        request = self.api._base_request('updateCustomerProfileRequest')
        profile = create_profile(customer)
        E.SubElement(profile, 'customerProfileId').text = customer_id
        request.append(profile)
        return request

    def _delete_request(self, customer_id):
        request = self.api._base_request('deleteCustomerProfileRequest')
        E.SubElement(request, 'customerProfileId').text = customer_id
        return request
