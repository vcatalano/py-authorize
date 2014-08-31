import xml.etree.cElementTree as E

try:
    import urllib.parse as urllib
except:
    import urllib

from authorize.apis.base_api import BaseAPI
from authorize.schemas import AIMTransactionSchema
from authorize.schemas import CIMTransactionSchema
from authorize.schemas import CreditTransactionSchema
from authorize.schemas import RefundTransactionSchema
from authorize.xml_data import *


class TransactionAPI(BaseAPI):

    def sale(self, params={}):
        if 'customer_id' in params:
            xact = self._deserialize(CIMTransactionSchema(), params)
            return self.api._make_call(self._cim_base_request('profileTransAuthCapture', xact))
        else:
            xact = self._deserialize(AIMTransactionSchema(), params)
            return self.api._make_call(self._aim_base_request('authCaptureTransaction', xact))

    def auth(self, params={}):
        if 'customer_id' in params:
            xact = self._deserialize(CIMTransactionSchema(), params)
            return self.api._make_call(self._cim_base_request('profileTransAuthOnly', xact))
        else:
            xact = self._deserialize(AIMTransactionSchema(), params)
            return self.api._make_call(self._aim_base_request('authOnlyTransaction', xact))

    def settle(self, transaction_id, amount=None):
        return self.api._make_call(self._settle_request(transaction_id, amount))

    def credit(self, params={}):
        xact = self._deserialize(CreditTransactionSchema(), params)
        return self.api._make_call(self._cim_base_request('profileTransRefund', xact))

    def refund(self, params={}):
        xact = self._deserialize(RefundTransactionSchema(), params)
        return self.api._make_call(self._refund_request(xact))

    def void(self, transaction_id):
        return self.api._make_call(self._void_request(transaction_id))

    def details(self, transaction_id):
        return self.api._make_call(self._details_request(transaction_id))

    def list(self, batch_id):
        if batch_id:
            return self.api._make_call(self._settled_list_request(batch_id))
        else:
            return self.api._make_call(self._unsettled_list_request())

    # The following methods generate the XML for the corresponding API calls.
    # This makes unit testing each of the calls easier.
    def _cim_base_request(self, xact_type, xact={}):
        request = self.api._base_request('createCustomerProfileTransactionRequest')

        xact_elem = E.SubElement(request, 'transaction')
        xact_type = E.SubElement(xact_elem, xact_type)

        E.SubElement(xact_type, 'amount').text = quantize(xact['amount'])

        if 'tax' in xact:
            xact_type.append(create_amount_type('tax', xact['tax']))

        if 'shipping_and_handling' in xact:
            xact_type.append(create_amount_type('shipping', xact['shipping_and_handling']))

        if 'duty' in xact:
            xact_type.append(create_amount_type('duty', xact['duty']))

        if 'line_items' in xact:
            for line_item in xact['line_items']:
                xact_type.append(create_line_item('lineItems', line_item))

        # CIM information
        E.SubElement(xact_type, 'customerProfileId').text = xact['customer_id']
        E.SubElement(xact_type, 'customerPaymentProfileId').text = xact['payment_id']

        if 'address_id' in xact:
            E.SubElement(xact_type, 'customerShippingAddressId').text = xact['address_id']

        if 'order' in xact:
            xact_type.append(create_order(xact['order']))

        if 'tax_exempt' in xact:
            E.SubElement(xact_type, 'taxExempt').text = str(xact['tax_exempt']).lower()

        if 'recurring' in xact:
            E.SubElement(xact_type, 'recurringBilling').text = str(xact['recurring']).lower()

        if 'extra_options' in xact:
            extra_options = {}
            if 'customer_ip' in xact['extra_options']:
                extra_options['x_customer_ip'] = xact['extra_options']['customer_ip']
            options = E.SubElement(request, 'extraOptions')
            E.SubElement(options, '![CDATA[').text = urllib.urlencode(extra_options)

        return request

    def _aim_base_request(self, xact_type, xact={}):
        request = self.api._base_request('createTransactionRequest')

        xact_elem = E.SubElement(request, 'transactionRequest')
        E.SubElement(xact_elem, 'transactionType').text = xact_type
        E.SubElement(xact_elem, 'amount').text = quantize(xact['amount'])

        payment = E.SubElement(xact_elem, 'payment')
        if 'credit_card' in xact:
            payment.append(create_card(xact['credit_card']))
        elif 'track_data' in xact:
            payment.append(format_tracks(xact['track_data']))
        else:
            payment.append(create_account(xact['bank_account']))

        if 'order' in xact:
            xact_elem.append(create_order(xact['order']))

        if 'line_items' in xact:
            xact_elem.append(create_line_items(xact['line_items']))

        if 'tax' in xact:
            xact_elem.append(create_amount_type('tax', xact['tax']))

        if 'duty' in xact:
            xact_elem.append(create_amount_type('duty', xact['duty']))

        if 'shipping_and_handling' in xact:
            xact_elem.append(create_amount_type('shipping', xact['shipping_and_handling']))

        if 'tax_exempt' in xact:
            E.SubElement(xact_elem, 'taxExempt').text = str(xact['tax_exempt']).lower()

        if 'email' in xact:
            customer = E.SubElement(xact_elem, 'customer')
            E.SubElement(customer, 'email').text = xact['email']

        if 'billing' in xact:
            xact_elem.append(create_address('billTo', xact['billing']))

        if 'shipping' in xact:
            xact_elem.append(create_address('shipTo', xact['shipping']))

        if 'extra_options' in xact:
            if 'customer_ip' in xact['extra_options']:
                E.SubElement(xact_elem, 'customerIP').text = xact['extra_options']['customer_ip']

        if 'retail' in xact:
            xact_elem.append(set_retail(xact['retail']))

        return request

    def _settle_request(self, transaction_id, amount):
        request = self.api._base_request('createTransactionRequest')
        xact_elem = E.SubElement(request, 'transactionRequest')
        E.SubElement(xact_elem, 'transactionType').text = 'priorAuthCaptureTransaction'

        if amount:
            E.SubElement(xact_elem, 'amount').text = quantize(amount)

        E.SubElement(xact_elem, 'refTransId').text = transaction_id
        return request

    def _refund_request(self, xact):
        request = self.api._base_request('createTransactionRequest')
        xact_elem = E.SubElement(request, 'transactionRequest')
        E.SubElement(xact_elem, 'transactionType').text = 'refundTransaction'
        E.SubElement(xact_elem, 'amount').text = quantize(xact['amount'])
        payment = E.SubElement(xact_elem, 'payment')
        credit_card = E.SubElement(payment, 'creditCard')
        E.SubElement(credit_card, 'cardNumber').text = xact['last_four'][-4:]
        # Authorize.net doesn't care about the actual date
        E.SubElement(credit_card, 'expirationDate').text = 'XXXXXX'
        E.SubElement(xact_elem, 'refTransId').text = xact['transaction_id']
        return request

    def _void_request(self, transaction_id):
        request = self.api._base_request('createTransactionRequest')
        xact_elem = E.SubElement(request, 'transactionRequest')
        E.SubElement(xact_elem, 'transactionType').text = 'voidTransaction'
        E.SubElement(xact_elem, 'refTransId').text = transaction_id
        return request

    def _details_request(self, transaction_id):
        request = self.api._base_request('getTransactionDetailsRequest')
        E.SubElement(request, 'transId').text = transaction_id
        return request

    def _unsettled_list_request(self):
        request = self.api._base_request('getUnsettledTransactionListRequest')
        return request

    def _settled_list_request(self, batch_id):
        request = self.api._base_request('getTransactionListRequest')
        E.SubElement(request, 'batchId').text = batch_id
        return request
