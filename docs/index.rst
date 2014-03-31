Py-Authorize
============

Py-Authorize is a full-featured Python API for the Authorize.net payment
gateway. Authorize.net offers great payment processing capabilities with a 
terribly incoherent API. Py-Authorize attempts to alleviate many of the
problems programmers might experience with Authorize.net's'API by providing a 
cleaner, simpler and much more coherent API.

Py-Authorize supports most all of the Authorize.net's API functionality 
including:

- Advanced Integration Method (AIM)
- Customer Integration Manager (CIM)
- Transaction Detail API/Reporting
- Automated Recurring Billing API (ARB)

Here is a simple example of a basic credit card transaction.

.. code-block:: python

    import authorize

    authorize.Configuration.configure(
        authorize.Environment.TEST,
        'api_login_id',
        'api_transaction_key',
    )

    result = authorize.Transaction.sale({
        'amount': 40.00,
        'credit_card': {
            'card_number': '4111111111111111',
            'expiration_date': '04/2014',
            'card_code': '343',
        }
    })

    result.transaction_response.trans_id
    # e.g. '2194343352'

Py-Authorize is released under the `MIT License`_.

.. _MIT License: http://www.opensource.org/licenses/mit-license


Contents:

.. toctree::
    :maxdepth: 1

    install
    getting_started
    transaction
    customer
    credit_card
    bank_account
    address
    recurring
    batch
    advanced
    development
