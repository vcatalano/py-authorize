import json
import re


RENAME_FIELDS = {
    'customerProfileId': 'customer_id',
    'customerPaymentProfileId': 'payment_id',
    'customerAddressId': 'address_id',
    'customerShippingAddressId': 'address_id',
    'customerPaymentProfileIdList': 'payment_ids',
    'customerShippingAddressIdList': 'address_ids',
    'validationDirectResponseList': 'validation_responses',
    'purchaseOrderNumber': 'order_number',
    'paymentProfiles': 'payments',
    'shipToList': 'addresses',
    'ids': 'profile_ids',
    'shipping': 'shipping_and_handling',
    'directResponse': 'transaction_response',
}

# XML Schema sequence element
LIST_FIELDS = [
    'messages',
    'shipToList',
    'paymentProfiles',
]

# Array of complex schema types
NESTED_LIST_FIELDS = [
    'ids',
    'errors',
    'customerPaymentProfileIdList',
    'customerShippingAddressIdList',
    'transactions',
    'batchList',
    'statistics',
]

DIRECT_RESPONSE_FIELDS = {
    0: 'response_code',
    2: 'response_reason_code',
    3: 'response_reason_text',
    4: 'authorization_code',
    5: 'avs_response',
    6: 'trans_id',
    9: 'amount',
    11: 'transaction_type',
    38: 'cvv_result_code',
}

FIRST_CAP_RE = re.compile('(.)([A-Z][a-z]+)')
ALL_CAP_RE = re.compile('([a-z0-9])([A-Z])')


class AttrDict(dict):

    def __init__(self, *args, **kw):
        dict.__init__(self, *args, **kw)

    def __getattr__(self, key):
        return self[key]

    def __setattr__(self, key, value):
        self[key] = value

    def __str__(self):
        return json.dumps(self, indent=2)


# Use lower_case_with_underscores to keep key names consistent
def rename(name):
    if name in RENAME_FIELDS:
        name = RENAME_FIELDS[name]
    name = FIRST_CAP_RE.sub(r'\1_\2', name)
    name = ALL_CAP_RE.sub(r'\1_\2', name)
    return name.lower()


def parse_direct_response(response_text):
    response = response_text.text.split(',')
    fields = AttrDict()
    for index, name in DIRECT_RESPONSE_FIELDS.items():
        fields[name] = response[index]
    return fields


def parse_response(element):
    # Remove the namespace qualifier
    key = element.tag[41:]

    if key == 'directResponse':
        return parse_direct_response(element)

    if len(element) == 0:
        return element.text

    dict_items = AttrDict()
    is_nested = key in NESTED_LIST_FIELDS

    for child in element:
        key = child.tag[41:]
        new_item = parse_response(child)

        if is_nested:
            # Ignore the current element and treat as a list item
            if isinstance(dict_items, list):
                dict_items.append(new_item)
            else:
                dict_items = [new_item]
        elif key in LIST_FIELDS:
            try:
                dict_items[rename(key)].append(new_item)
            except:
                dict_items[rename(key)] = [new_item]
        else:
            dict_items[rename(key)] = new_item

    return dict_items