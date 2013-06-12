import xml.etree.cElementTree as E

from authorize.apis.base_api import BaseAPI
from authorize.schemas import AddressSchema
from authorize.xml_data import *


class AddressAPI(BaseAPI):

    def create(self, customer_id, params={}):
        address = self._deserialize(AddressSchema(), params)
        return self.api._make_call(self._create_request(customer_id, address))

    def details(self, customer_id, address_id):
        return self.api._make_call(self._details_request(customer_id, address_id))

    def update(self, customer_id, address_id, params={}):
        address = self._deserialize(AddressSchema(), params)
        return self.api._make_call(self._update_request(customer_id, address_id, address))

    def delete(self, customer_id, address_id):
        self.api._make_call(self._delete_request(customer_id, address_id))

    # The following methods generate the XML for the corresponding API calls.
    # This makes unit testing each of the calls easier.
    def _create_request(self, customer_id, address={}):
        return self._make_xml('createCustomerShippingAddressRequest', customer_id, None, params=address)

    def _details_request(self, customer_id, address_id):
        request = self.api._base_request('getCustomerShippingAddressRequest')
        E.SubElement(request, 'customerProfileId').text = customer_id
        E.SubElement(request, 'customerAddressId').text = address_id
        return request

    def _update_request(self, customer_id, address_id, address={}):
        return self._make_xml('updateCustomerShippingAddressRequest', customer_id, address_id, params=address)

    def _delete_request(self, customer_id, address_id):
        request = self.api._base_request('deleteCustomerShippingAddressRequest')
        E.SubElement(request, 'customerProfileId').text = customer_id
        E.SubElement(request, 'customerAddressId').text = address_id
        return request

    def _make_xml(self, method, customer_id=None, address_id=None, params={}):
        request = self.api._base_request(method)

        if customer_id:
            E.SubElement(request, 'customerProfileId').text = customer_id

        address_data = create_address('address', params)

        if address_id:
            E.SubElement(address_data, 'customerAddressId').text = address_id

        request.append(address_data)

        return request
