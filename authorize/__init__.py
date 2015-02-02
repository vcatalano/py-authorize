import xml.etree.ElementTree as E

from authorize.configuration import Configuration
from authorize.address import Address
from authorize.bank_account import BankAccount
from authorize.batch import Batch
from authorize.credit_card import CreditCard
from authorize.customer import Customer
from authorize.environment import Environment
from authorize.exceptions import AuthorizeError
from authorize.exceptions import AuthorizeConnectionError
from authorize.exceptions import AuthorizeResponseError
from authorize.exceptions import AuthorizeInvalidError
from authorize.recurring import Recurring
from authorize.transaction import Transaction


# Monkeypatch the ElementTree module so that we can use CDATA element types
E._original_serialize_xml = E._serialize_xml
def _serialize_xml(write, elem, *args, **kwargs):
    if elem.tag == '![CDATA[':
        write('<![CDATA[%s]]>' % elem.text)
        return
    return E._original_serialize_xml(write, elem, *args, **kwargs)
E._serialize_xml = E._serialize['xml'] = _serialize_xml
