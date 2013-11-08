import json
import re


RENAME_FIELDS = {
    'customerProfileId': 'customer_id',
    'customerPaymentProfileId': 'payment_id',
    'customerAddressId': 'address_id',
    'customerShippingAddressId': 'address_id',
    'customerPaymentProfileIdList': 'payment_ids',
    'customerShippingAddressIdList': 'address_ids',
    'shipToList': 'addresses',
    'ids': 'profile_ids',
    'shipping': 'shipping_and_handling',
    'directResponse': 'transaction_response',
}

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


def underscore(name):
    first_string = FIRST_CAP_RE.sub(r'\1_\2', name)
    return ALL_CAP_RE.sub(r'\1_\2', first_string).lower()


def parse_direct_response(response):
    response = response.text.split(',')
    fields = AttrDict()
    for index, name in DIRECT_RESPONSE_FIELDS.items():
        fields[name] = response[index]
    return fields


def parse_response(element):
    key = element.tag[41:]

    if key.endswith('List') or key == 'ids' or key == 'transactions':
        list_items = []
        for child in element:
            list_items.append(parse_response(child))
        return list_items
    elif key == 'directResponse':
        return parse_direct_response(element)
    elif len(element) > 0:
        dict_items = AttrDict()
        for child in element:
            child_elem = parse_response(child)
            key = child.tag[41:]
            # Rename response fields
            if key in RENAME_FIELDS:
                key = RENAME_FIELDS[key]
            key = underscore(key)
            dict_items[key] = child_elem
        return dict_items
    else:
        return element.text
