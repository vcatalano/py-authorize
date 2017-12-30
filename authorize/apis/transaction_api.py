try:
    import urllib.parse as urllib
except:
    import urllib

from authorize.apis.base_api import BaseAPI
from authorize.schemas import AIMTransactionSchema
from authorize.schemas import CreditTransactionSchema
from authorize.schemas import RefundTransactionSchema
from authorize.xml_data import *


class TransactionAPI(BaseAPI):

    def sale(self, params={}):
        xact = self._deserialize(AIMTransactionSchema(), params)
        return self.api._make_call(self._transaction_request('authCaptureTransaction', xact))

    def auth(self, params={}):
        xact = self._deserialize(AIMTransactionSchema(), params)
        return self.api._make_call(self._transaction_request('authOnlyTransaction', xact))

    def settle(self, transaction_id, amount=None):
        return self.api._make_call(self._settle_request(transaction_id, amount))

    def credit(self, params={}):
        xact = self._deserialize(CreditTransactionSchema(), params)
        return self.api._make_call(self._transaction_request('refundTransaction', xact))

    def auth_continue(self, transaction_id, payer_id):
        return self.api._make_call(self._pay_pal_continue_request('authOnlyContinueTransaction', transaction_id,
                                                                  payer_id))

    def sale_continue(self, transaction_id, payer_id):
        return self.api._make_call(self._pay_pal_continue_request('authCaptureContinueTransaction', transaction_id,
                                                                  payer_id))

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

    def _transaction_request(self, xact_type, xact={}):
        is_cim = 'customer_id' in xact

        request = self.api._base_request('createTransactionRequest')

        xact_elem = E.SubElement(request, 'transactionRequest')
        E.SubElement(xact_elem, 'transactionType').text = xact_type
        E.SubElement(xact_elem, 'amount').text = quantize(xact['amount'])

        if 'currency_code' in xact:
            E.SubElement(xact_elem, 'currencyCode').text = xact['currency_code']

        # CIM information
        if is_cim:  # customerProfilePaymentType
            profile = E.SubElement(xact_elem, 'profile')

            # TODO - determine how to create a new customer here...

            E.SubElement(profile, 'customerProfileId').text = xact['customer_id']

            payment = E.SubElement(profile, 'paymentProfile')
            E.SubElement(payment, 'paymentProfileId').text = xact['payment_id']

            if 'address_id' in xact:
                E.SubElement(profile, 'shippingProfileId').text = xact['address_id']
        else:
            payment = E.SubElement(xact_elem, 'payment')
            if 'credit_card' in xact:
                payment.append(create_card(xact['credit_card']))
            elif 'track_data' in xact:
                payment.append(format_tracks(xact['track_data']))
            elif 'bank_account' in xact:
                payment.append(create_account(xact['bank_account']))
            elif 'pay_pal' in xact:
                payment.append(create_pay_pal(xact['pay_pal']))

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

        if 'po_number' in xact:
            E.SubElement(xact_elem, 'poNumber').text = xact['po_number']

        if 'email' in xact:
            customer = E.SubElement(xact_elem, 'customer')
            E.SubElement(customer, 'email').text = xact['email']

        if not is_cim and 'billing' in xact:
            xact_elem.append(create_address('billTo', xact['billing']))

        if not is_cim and 'shipping' in xact:
            xact_elem.append(create_address('shipTo', xact['shipping']))

        if 'customer_ip' in xact:
            E.SubElement(xact_elem, 'customerIP').text = xact['customer_ip']

        if 'retail' in xact:
            xact_elem.append(set_retail(xact['retail']))

        if 'user_fields' in xact:
            xact_elem.append(create_user_fields(xact['user_fields']))

        return request

    def _settle_request(self, transaction_id, amount):
        request = self.api._base_request('createTransactionRequest')
        xact_elem = E.SubElement(request, 'transactionRequest')
        E.SubElement(xact_elem, 'transactionType').text = 'priorAuthCaptureTransaction'

        if amount:
            E.SubElement(xact_elem, 'amount').text = quantize(amount)

        E.SubElement(xact_elem, 'refTransId').text = transaction_id
        return request

    def _pay_pal_continue_request(self, xact_type, transaction_id, payer_id):
        request = self.api._base_request('createTransactionRequest')
        xact_elem = E.SubElement(request, 'transactionRequest')
        E.SubElement(xact_elem, 'transactionType').text = xact_type

        payment = E.Element('payment')
        pay_pal = E.SubElement(payment, 'payPal')
        E.SubElement(pay_pal, 'payerID').text = payer_id
        xact_elem.append(payment)

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
        if 'order' in xact:
            xact_elem.append(create_order(xact['order']))
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
