import xml.etree.cElementTree as E

from decimal import Decimal
from xml.dom import minidom


def create_profile(params={}):
    profile = E.Element('profile')
    E.SubElement(profile, 'merchantCustomerId').text = params['merchant_id']
    if 'description' in params:
        E.SubElement(profile, 'description').text = params['description']
    if 'email' in params:
        E.SubElement(profile, 'email').text = params['email']
    return profile


def create_customer(params={}):
    customer = E.Element('customer')
    E.SubElement(customer, 'merchantCustomerId').text = params['merchant_id']
    if 'description' in params:
        E.SubElement(customer, 'description').text = params['description']
    if 'email' in params:
        E.SubElement(customer, 'email').text = params['email']
    return customer


def create_address(name, params={}):
    address = E.Element(name)
    if 'first_name' in params:
        E.SubElement(address, 'firstName').text = params['first_name']
    if 'last_name' in params:
        E.SubElement(address, 'lastName').text = params['last_name']
    if 'company' in params:
        E.SubElement(address, 'company').text = params['company']
    if 'address' in params:
        E.SubElement(address, 'address').text = params['address']
    if 'city' in params:
        E.SubElement(address, 'city').text = params['city']
    if 'state' in params:
        E.SubElement(address, 'state').text = params['state']
    if 'zip' in params:
        E.SubElement(address, 'zip').text = params['zip']
    if 'country' in params:
        E.SubElement(address, 'country').text = params['country']
    if 'phone_number' in params:
        E.SubElement(address, 'phoneNumber').text = params['phone_number']
    if 'fax_number' in params:
        E.SubElement(address, 'faxNumber').text = params['fax_number']
    return address


def create_card(params={}):
    card = E.Element('creditCard')
    date = params['expiration_year'] + '-' + params['expiration_month']
    E.SubElement(card, 'cardNumber').text = params['card_number']
    E.SubElement(card, 'expirationDate').text = date
    if 'card_code' in params:
        E.SubElement(card, 'cardCode').text = str(params['card_code'])
    return card


def create_opaque_data(params={}):
    data = E.Element('opaqueData')
    E.SubElement(data, 'dataDescriptor').text = params['data_descriptor']
    E.SubElement(data, 'dataValue').text = params['data_value']
    if 'data_key' in params:
        E.SubElement(data, 'dataKey').text = str(params['data_key'])
    return data


def format_tracks(params={}):
    tracks = E.Element('trackData')
    if 'track_1' in params:
        E.SubElement(tracks, 'track1').text = params['track_1']
    elif 'track_2' in params:
        E.SubElement(tracks, 'track2').text = params['track_2']
    return tracks


def set_retail(params={}):
    retail = E.Element('retail')
    E.SubElement(retail, 'marketType').text = str(params['market_type'])
    E.SubElement(retail, 'deviceType').text = str(params['device_type'])
    return retail


def create_account(params={}):
    account = E.Element('bankAccount')
    if 'account_type' in params:
        E.SubElement(account, 'accountType').text = params['account_type']
    E.SubElement(account, 'routingNumber').text = params['routing_number']
    E.SubElement(account, 'accountNumber').text = params['account_number']
    E.SubElement(account, 'nameOnAccount').text = params['name_on_account']
    if 'echeck_type' in params:
        E.SubElement(account, 'echeckType').text = params['echeck_type']
    if 'bank_name' in params:
        E.SubElement(account, 'bankName').text = params['bank_name']
    return account


def create_pay_pal(params={}):
    pay_pal = E.Element('payPal')
    if 'success_url' in params:
        E.SubElement(pay_pal, 'successUrl').text = params['success_url']
    if 'cancel_url' in params:
        E.SubElement(pay_pal, 'cancelUrl').text = params['cancel_url']
    if 'locale' in params:
        E.SubElement(pay_pal, 'paypalLc').text = params['locale']
    if 'header_image' in params:
        E.SubElement(pay_pal, 'paypalHdrImg').text = params['header_image']
    if 'flow_color' in params:
        E.SubElement(pay_pal, 'paypalPayflowcolor').text = params['flow_color']
    return pay_pal


def create_line_item(name, params={}):
    item = E.Element(name)
    if 'item_id' in params:
        E.SubElement(item, 'itemId').text = params['item_id']
    if 'name' in params:
        E.SubElement(item, 'name').text = params['name']
    if 'description' in params:
        E.SubElement(item, 'description').text = params['description']
    if 'quantity' in params:
        E.SubElement(item, 'quantity').text = str(params['quantity'])
    if 'unit_price' in params:
        E.SubElement(item, 'unitPrice').text = quantize(params['unit_price'])
    if 'taxable' in params:
        E.SubElement(item, 'taxable').text = str(params['taxable']).lower()
    return item


def create_line_items(items=[]):
    line_items = E.Element('lineItems')
    for item in items:
        line_items.append(create_line_item('lineItem', item))
    return line_items


def create_user_fields(fields=[]):
    user_fields = E.Element('userFields')
    for field in fields:
        item = E.Element('userField')
        E.SubElement(item, 'name').text = field['name']
        E.SubElement(item, 'value').text = field['value']
        user_fields.append(item)
    return user_fields


def create_amount_type(name, params={}):
    amount_type = E.Element(name)
    if 'amount' in params:
        E.SubElement(amount_type, 'amount').text = quantize(params['amount'])
    if 'name' in params:
        E.SubElement(amount_type, 'name').text = params['name']
    if 'description' in params:
        E.SubElement(amount_type, 'description').text = params['description']
    return amount_type


def create_order(params={}):
    order = E.Element('order')
    if 'invoice_number' in params:
        E.SubElement(order, 'invoiceNumber').text = params['invoice_number']
    if 'description' in params:
        E.SubElement(order, 'description').text = params['description']
    return order


def create_payment(params={}):
    payment = E.Element('payment')
    # If a card_number key exists here, we know that we are dealing with a
    # credit card. Otherwise, it's a bank account.
    if 'card_number' in params:
        payment.append(create_card(params))
    elif 'track_data' in params:
        payment.append(format_tracks(params))
    elif 'data_descriptor' in params:
        payment.append(create_opaque_data(params))
    else:
        payment.append(create_account(params))
    return payment


def create_transaction_settings(params):
    e = E.Element('transactionSettings')
    if 'duplicate_window' in params:
        e.append(create_transaction_setting('duplicateWindow', str(params['duplicate_window'])))
    return e


def create_transaction_setting(name, value):
    e = E.Element('setting')
    E.SubElement(e, 'settingName').text = name
    E.SubElement(e, 'settingValue').text = value
    return e


def quantize(amount):
    return str(Decimal(str(amount)).quantize(Decimal('0.01')))


def prettify(elem):
    """Return a pretty-printed XML string for the Element."""
    rough_string = E.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent='  ').strip()
