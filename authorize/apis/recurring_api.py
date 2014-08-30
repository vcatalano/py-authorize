import xml.etree.cElementTree as E

from authorize.apis.base_api import BaseAPI
from authorize.schemas import CreateRecurringSchema
from authorize.schemas import UpdateRecurringSchema
from authorize.xml_data import *


class RecurringAPI(BaseAPI):

    def create(self, params={}):
        subscription = self._deserialize(CreateRecurringSchema().bind(), params)
        return self.api._make_call(self._create_request(subscription))

    def details(self, subscription_id):
        return self.api._make_call(self._details_request(subscription_id))

    def update(self, subscription_id, params={}):
        subscription = self._deserialize(UpdateRecurringSchema().bind(), params)
        return self.api._make_call(self._update_request(subscription_id, subscription))

    def delete(self, subscription_id):
        self.api._make_call(self._delete_request(subscription_id))

    # The following methods generate the XML for the corresponding API calls.
    # This makes unit testing each of the calls easier.
    def _create_request(self, subscription={}):
        return self._make_xml('ARBCreateSubscriptionRequest', None, params=subscription)

    def _details_request(self, subscription_id):
        request = self.api._base_request('ARBGetSubscriptionStatusRequest')
        E.SubElement(request, 'subscriptionId').text = subscription_id
        return request

    def _update_request(self, subscription_id, subscription={}):
        return self._make_xml('ARBUpdateSubscriptionRequest', subscription_id, params=subscription)

    def _delete_request(self, subscription_id):
        request = self.api._base_request('ARBCancelSubscriptionRequest')
        E.SubElement(request, 'subscriptionId').text = subscription_id
        return request

    def _make_xml(self, method, subscription_id=None, params={}):
        request = self.api._base_request(method)

        if subscription_id:
            E.SubElement(request, 'subscriptionId').text = subscription_id

        subscription = E.SubElement(request, 'subscription')

        if 'name' in params:
            E.SubElement(subscription, 'name').text = params['name']

        # Payment schedule
        schedule = E.SubElement(subscription, 'paymentSchedule')
        if subscription_id is None:
            interval = E.SubElement(schedule, 'interval')
            E.SubElement(interval, 'length').text = str(params['interval_length'])
            E.SubElement(interval, 'unit').text = params['interval_unit']

        if 'start_date' in params:
            E.SubElement(schedule, 'startDate').text = str(params['start_date'])

        if 'total_occurrences' in params:
            E.SubElement(schedule, 'totalOccurrences').text = str(params['total_occurrences'])

        if 'trial_occurrences' in params:
            E.SubElement(schedule, 'trialOccurrences').text = str(params['trial_occurrences'])

        if 'amount' in params:
            E.SubElement(subscription, 'amount').text = quantize(params['amount'])

        if 'trial_amount' in params:
            E.SubElement(subscription, 'trialAmount').text = quantize(params['trial_amount'])

        # Payment information
        if 'credit_card' in params:
            subscription.append(create_payment(params['credit_card']))
        else:
            subscription.append(create_payment(params['bank_account']))

        if 'order' in params:
            subscription.append(create_order(params['order']))

        if 'customer' in params:
            customer = E.SubElement(subscription, 'customer')
            E.SubElement(customer, 'id').text = params['customer']['merchant_id']
            if 'email' in params['customer']:
                E.SubElement(customer, 'email').text = params['customer']['email']

        # A very obscure bug exists that will throw an error if no last name
        # or first name is provided for billing.
        # Issue 26: Don't set these billing fields if there is already a 
        # subscription.
        if subscription_id is None:
            arb_required_fields = {
                'billing': {
                    'first_name': '<empty>',
                    'last_name': '<empty>'
                }
            }
            arb_required_fields.update(params)
            params = arb_required_fields

        if 'billing' in params:
            subscription.append(create_address('billTo', params['billing']))

        if 'shipping' in params:
            subscription.append(create_address('shipTo', params['shipping']))

        return request
