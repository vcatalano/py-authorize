import colander

from datetime import date
from uuid import uuid4


@colander.deferred
def merchant_id(node, kw):
    return uuid4().hex[:20]


@colander.deferred
def today(node, kw):
    return date.today().isoformat()


class AddressSchema(colander.MappingSchema):
    first_name = colander.SchemaNode(colander.String(),
                                     validator=colander.Length(max=50),
                                     missing=colander.drop)
    last_name = colander.SchemaNode(colander.String(),
                                    validator=colander.Length(max=50),
                                    missing=colander.drop)
    company = colander.SchemaNode(colander.String(),
                                  validator=colander.Length(max=50),
                                  missing=colander.drop)
    address = colander.SchemaNode(colander.String(),
                                  validator=colander.Length(max=60),
                                  missing=colander.drop)
    city = colander.SchemaNode(colander.String(),
                               validator=colander.Length(max=40),
                               missing=colander.drop)
    state = colander.SchemaNode(colander.String(),
                                validator=colander.Length(max=40),
                                missing=colander.drop)
    zip = colander.SchemaNode(colander.String(),
                              validator=colander.Length(max=20),
                              missing=colander.drop)
    country = colander.SchemaNode(colander.String(),
                                  validator=colander.Length(max=60),
                                  missing=colander.drop)
    phone_number = colander.SchemaNode(colander.String(),
                                       validator=colander.Length(max=25),
                                       missing=colander.drop)
    fax_number = colander.SchemaNode(colander.String(),
                                     validator=colander.Length(max=25),
                                     missing=colander.drop)


class CreditCardSchema(colander.MappingSchema):
    card_number = colander.SchemaNode(colander.String(),
                                      validator=colander.luhnok,
                                      required=True)
    expiration_month = colander.SchemaNode(colander.Integer(),
                                           validator=colander.Range(1, 12),
                                           missing=None)
    expiration_year = colander.SchemaNode(colander.Integer(),
                                          validator=colander.Range(date.today().year,
                                                                   date.today().year + 7),
                                          missing=None)
    expiration_date = colander.SchemaNode(colander.String(),
                                          validator=colander.Regex(
                                          r'^\d{2}.?(?:\d{4}|\d{2})?$', 'The expiration date is invalid'),
                                          missing=None)
    card_code = colander.SchemaNode(colander.String(),
                                    validator=colander.Regex(
                                    r'^[0-9]{3,4}$', 'The card code is invalid'),
                                    missing=colander.drop)

    @staticmethod
    def validator(node, kw):
        exp_year = kw['expiration_year']
        exp_month = kw['expiration_month']
        exp_date = kw['expiration_date']

        # We only need exp_date or exp_year and exp_month
        if exp_date is None and (exp_year is None and exp_month is None):
            raise colander.Invalid(node, 'You must provide a card expiration date')

        if exp_date is not None:
            exp_month = exp_date[:2]
            exp_year = '20' + exp_date[-2:]
        elif exp_month is None:
            raise colander.Invalid(node, 'You must provide a card expiration month')
        elif exp_year is None:
            raise colander.Invalid(node, 'You must provide a card expiration year')

        today = date.today()
        if exp_year == today.year and exp_month < today.month:
            raise colander.Invalid(node, 'The credit card has expired')

        kw['expiration_year'] = str(exp_year)
        kw['expiration_month'] = str(exp_month).zfill(2)


class TrackDataSchema(colander.MappingSchema):
    track_1 = colander.SchemaNode(colander.String(),
                                  validator=colander.Regex(
                                  r'^%?B\d{1,19}\^[A-Z /]{2,26}\^(\d|\^){4}(\d|\^){3}.*\??$', 'Track 1 does not match IATA format'),
                                  missing=colander.drop,
                                  required=None)
    track_2 = colander.SchemaNode(colander.String(),
                                  validator=colander.Regex(
                                  r'^;?\d{1,19}=(\d|=){4}(\d|=){3}.*\??$', 'Track 2 does not match ABA format'),
                                  missing=colander.drop,
                                  required=None)

    @staticmethod
    def validator(node, kw):
        track1 = kw.get('track_1', None)
        track2 = kw.get('track_2', None)
        if track1 is None and track2 is None:
            raise colander.Invalid(node, "You must provide at least one track")
        if track1:
            kw['track_1'] = str(track1).lstrip('%').rstrip('?')
        if track2:
            kw['track_2'] = str(track2).lstrip(';').rstrip('?')


class RetailSchema(colander.MappingSchema):
    market_type = colander.SchemaNode(colander.Integer(),
                                      validator=colander.Range(1, 9),
                                      required=True)
    device_type = colander.SchemaNode(colander.Integer(),
                                      validator=colander.Range(1, 9),
                                      required=True)

    @staticmethod
    def validator(node, kw):
        kw['market_type'] = kw.get('market_type', 2)
        kw['device_type'] = kw.get('device_type', 7)



class BankAccountSchema(colander.MappingSchema):
    account_type = colander.SchemaNode(colander.String(),
                                       validator=colander.OneOf(['checking', 'savings', 'businessChecking']),
                                       missing=colander.drop)
    routing_number = colander.SchemaNode(colander.String(),
                                         validator=colander.Regex(r'^[\d+]{9}$', 'The routing number is invalid'),
                                         required=True)
    account_number = colander.SchemaNode(colander.String(),
                                         validator=colander.Regex(r'^[\d+]{5,17}$', 'The account number is invalid'),
                                         required=True)
    name_on_account = colander.SchemaNode(colander.String(),
                                          validator=colander.Length(max=22),
                                          required=True)
    echeck_type = colander.SchemaNode(colander.String(),
                                      validator=colander.OneOf(['ARC', 'BOC', 'CCD', 'PPD', 'TEL', 'WEB']),
                                      missing=colander.drop)
    bank_name = colander.SchemaNode(colander.String(),
                                    validator=colander.Length(max=50),
                                    missing=colander.drop)


class CustomerTypeSchema(colander.MappingSchema):
    customer_type = colander.SchemaNode(colander.String(),
                                        validator=colander.OneOf(['individual', 'business']),
                                        missing=colander.drop)


class CreateCreditCardSchema(CreditCardSchema, CustomerTypeSchema):
    billing = AddressSchema(missing=colander.drop)


class UpdateCreditCardSchema(CreateCreditCardSchema):
    card_number = colander.SchemaNode(colander.String(),
                                      validator=colander.Length(min=4),
                                      required=True)


class ValidateCreditCardSchema(colander.MappingSchema):
    address_id = colander.SchemaNode(colander.String(),
                                     validator=colander.Length(max=60),
                                     missing=colander.drop)
    card_code = colander.SchemaNode(colander.String(),
                                    validator=colander.Regex(
                                    r'^[0-9]{3,4}$', 'The card code is invalid'),
                                    missing=colander.drop)
    # A test mode is required for this transaction type. By default, we will
    # use 'testMode'
    validation_mode = colander.SchemaNode(colander.String(),
                                          validator=colander.OneOf(['liveMode', 'testMode']),
                                          missing='testMode')


class CreateBankAccountSchema(BankAccountSchema, CustomerTypeSchema):
    billing = AddressSchema(missing=colander.drop)


class CustomerBaseSchema(colander.MappingSchema):
    merchant_id = colander.SchemaNode(colander.String(),
                                      validator=colander.Length(max=20),
                                      missing=merchant_id)
    description = colander.SchemaNode(colander.String(),
                                      validator=colander.Length(max=255),
                                      missing=colander.drop)
    email = colander.SchemaNode(colander.String(),
                                validator=colander.Email(),
                                missing=colander.drop)


class CustomerSchema(AddressSchema):
    email = colander.SchemaNode(colander.String(),
                                validator=colander.Email(),
                                missing=colander.drop)
    customer_id = colander.SchemaNode(colander.String(),
                                      validator=colander.Length(max=20),
                                      missing=colander.drop)


class CreateCustomerSchema(CustomerBaseSchema, CustomerTypeSchema):
    # Customer payment method (optional)
    credit_card = CreditCardSchema(validator=CreditCardSchema.validator,
                                   missing=colander.drop)
    bank_account = BankAccountSchema(validator=BankAccountSchema.validator,
                                     missing=colander.drop)

    # Customer address information
    billing = AddressSchema(missing=colander.drop)
    shipping = AddressSchema(missing=colander.drop)


class AmountItemSchema(colander.MappingSchema):
    name = colander.SchemaNode(colander.String(),
                               validator=colander.Length(max=31),
                               missing=colander.drop)
    description = colander.SchemaNode(colander.String(),
                                      validator=colander.Length(max=255),
                                      missing=colander.drop)
    amount = colander.SchemaNode(colander.Decimal('0.01'),
                                 validator=colander.Range(min=0),
                                 missing=colander.drop)


class LineItemSchema(colander.MappingSchema):
    item_id = colander.SchemaNode(colander.String(),
                                  validator=colander.Length(max=31),
                                  missing=colander.drop)
    name = colander.SchemaNode(colander.String(),
                               validator=colander.Length(max=31),
                               missing=colander.drop)
    description = colander.SchemaNode(colander.String(),
                                      validator=colander.Length(max=255),
                                      missing=colander.drop)
    quantity = colander.SchemaNode(colander.Integer(),
                                   validator=colander.Range(min=0, max=99),
                                   missing=colander.drop)
    unit_price = colander.SchemaNode(colander.Decimal('0.01'),
                                     validator=colander.Range(min=0),
                                     missing=colander.drop)
    taxable = colander.SchemaNode(colander.Boolean(),
                                  missing=colander.drop)


class LineItemsSchema(colander.SequenceSchema):
    line_item = LineItemSchema()


class OrderSchema(colander.MappingSchema):
    invoice_number = colander.SchemaNode(colander.String(),
                                         validator=colander.Length(max=25),
                                         missing=colander.drop)
    description = colander.SchemaNode(colander.String(),
                                      validator=colander.Length(max=255),
                                      missing=colander.drop)
    order_number = colander.SchemaNode(colander.String(),
                                       validator=colander.Length(max=25),
                                       missing=colander.drop)


class ExtraOptions(colander.MappingSchema):
    customer_ip = colander.SchemaNode(colander.String(),
                                      validator=colander.Length(max=39),
                                      missing=colander.drop)


class TransactionBaseSchema(colander.MappingSchema):
    line_items = LineItemsSchema(validator=colander.Length(max=30),
                                 missing=colander.drop)
    order = OrderSchema(missing=colander.drop)
    tax = AmountItemSchema(missing=colander.drop)
    duty = AmountItemSchema(missing=colander.drop)
    shipping_and_handling = AmountItemSchema(missing=colander.drop)
    amount = colander.SchemaNode(colander.Decimal('0.01'),
                                 validator=colander.Range(0, 20000),
                                 required=True)
    split_tender_id = colander.SchemaNode(colander.String(),
                                          missing=colander.drop)
    tax_exempt = colander.SchemaNode(colander.Boolean(), missing=colander.drop)
    extra_options = ExtraOptions(missing=colander.drop)


class CIMBaseSchema(colander.MappingSchema):
    customer_id = colander.SchemaNode(colander.String(),
                                      validator=colander.Length(max=60),
                                      required=True)
    payment_id = colander.SchemaNode(colander.String(),
                                     validator=colander.Length(max=60),
                                     required=True)
    address_id = colander.SchemaNode(colander.String(),
                                     validator=colander.Length(max=60),
                                     missing=colander.drop)


class CIMTransactionSchema(CIMBaseSchema, TransactionBaseSchema):
    recurring = colander.SchemaNode(colander.Boolean(),
                                    missing=colander.drop)
    card_code = colander.SchemaNode(colander.String(),
                                    validator=colander.Regex(
                                    r'^[0-9]{3,4}$', 'The card code is invalid'),
                                    missing=colander.drop)


class AIMTransactionSchema(TransactionBaseSchema):
    email = colander.SchemaNode(colander.String(),
                                validator=colander.Email(),
                                missing=colander.drop)
    credit_card = CreditCardSchema(validator=CreditCardSchema.validator,
                                   missing=colander.drop)
    track_data = TrackDataSchema(validator=TrackDataSchema.validator,
                                 missing=colander.drop)
    retail = RetailSchema(validator=RetailSchema.validator,
                          missing=colander.drop)
    bank_account = BankAccountSchema(validator=BankAccountSchema.validator,
                                     missing=colander.drop)
    billing = AddressSchema(missing=colander.drop)
    shipping = AddressSchema(missing=colander.drop)
    customer = CustomerSchema(missing=colander.drop)


class CreditTransactionSchema(CIMBaseSchema):
    amount = colander.SchemaNode(colander.Decimal('0.01'),
                                 validator=colander.Range(0, 20000),
                                 required=True)


class RefundTransactionSchema(colander.MappingSchema):
    amount = colander.SchemaNode(colander.Decimal('0.01'),
                                 validator=colander.Range(0, 20000),
                                 required=True)
    transaction_id = colander.SchemaNode(colander.String(),
                                         validator=colander.Length(max=60),
                                         required=True)
    last_four = colander.SchemaNode(colander.String(),
                                    validator=colander.Length(max=16),
                                    required=True)


class ListBatchSchema(colander.MappingSchema):
    start = colander.SchemaNode(colander.Date(),
                                missing=colander.drop)
    end = colander.SchemaNode(colander.Date(),
                              missing=colander.drop)


class UpdateRecurringSchema(colander.MappingSchema):
    name = colander.SchemaNode(colander.String(),
                               validator=colander.Length(max=60),
                               missing=colander.drop)
    start_date = colander.SchemaNode(colander.Date(),
                                     missing=colander.drop)
    trial_amount = colander.SchemaNode(colander.Decimal('0.01'),
                                       validator=colander.Range(0, 20000),
                                       missing=colander.drop)
    total_occurrences = colander.SchemaNode(colander.Integer(),
                                            validator=colander.Range(1, 9999),
                                            missing=colander.drop)
    trial_occurrences = colander.SchemaNode(colander.Integer(),
                                            validator=colander.Range(1, 99),
                                            missing=colander.drop)

    credit_card = CreditCardSchema(validator=CreditCardSchema.validator,
                                   missing=colander.drop)
    bank_account = BankAccountSchema(validator=BankAccountSchema.validator,
                                     missing=colander.drop)
    customer = CustomerBaseSchema(missing=colander.drop)
    order = OrderSchema(missing=colander.drop)
    billing = AddressSchema(missing=colander.drop)
    shipping = AddressSchema(missing=colander.drop)


class CreateRecurringSchema(UpdateRecurringSchema):
    interval_length = colander.SchemaNode(colander.Integer(),
                                          validator=colander.Range(1, 999),
                                          required=True)
    interval_unit = colander.SchemaNode(colander.String(),
                                        validator=colander.OneOf(['days', 'months']),
                                        required=True)
    start_date = colander.SchemaNode(colander.Date(),
                                     missing=today)
    total_occurrences = colander.SchemaNode(colander.Integer(),
                                            validator=colander.Range(1, 9999),
                                            missing=9999)
    amount = colander.SchemaNode(colander.Decimal('0.01'),
                                 validator=colander.Range(0, 20000),
                                 required=True)


"""Additional validation functions"""


def require_payment_method(node, kw):
    """Ensures that a payment method is specified for the current node,"""
    if 'credit_card' not in kw and 'track_data' not in kw and 'bank_account' not in kw:
        raise colander.Invalid(node, 'You must provide either a credit card, some track data or a bank account')
