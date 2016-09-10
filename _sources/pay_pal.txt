PayPal Express Checkout
=======================

Authorize.net now provides functionality for PayPal Express Checkout. With
PayPal Express Checkout, you can accept payments with PayPal while utilizing
Authorize.net's reporting functionality.

For more detailed information about how the PayPal Express Checkout process
works with Authorize.net, visit the official `PayPal Express Checkout`_
documentation.

.. _PayPal Express Checkout:http://developer.authorize.net/api/reference/features/paypal.html


Additional API Flow Functions
-----------------------------

In order to handle the additional steps required by the PayPal Express Checkout
flow process, two additional functions have been added to the Transaction API:
``Transaction.auth_continue`` and ``Transaction.sale_continue``. These functions
refer to ``Authorize Only, Continue`` and ``Authorize and Capture, Continue``
requests, respectively.


Transaction Flow Sequence Example 1
-----------------------------------

#. Authorization Only
#. Get Details (recommended for shipping)
#. Authorization Only, Continue
#. Prior Authorization Capture
#. Refund (optional)

.. code-block:: python

    result = authorize.Transaction.auth({
        'amount': 40.00,
        'pay_pal': {
            'success_url': 'https://my.server.com/success.html',
            'cancel_url': 'https://my.server.com/cancel.html',
            'locale': 'US',
            'header_image': 'https://usa.visa.com/img/home/logo_visa.gif',
            'flow_color': 'FF0000'
        },
    })

    result.transaction_response.trans_id
    # e.g. 'transaction_id'

    result.secure_acceptance.secure_acceptance_url
    # e.g. https://www.paypal.com/cgibin/webscr?cmd=_express-checkout&token=EC-4WL17777V4111184H

    # (optional) get shipping information for order
    details = authorize.Transaction.details('transaction_id')

    authorize.Transaction.auth_continue('transaction_id', 'payer_id')

    authorize.Transaction.settle('transaction_id')

    # (optional) refund the transaction
    authorize.Transaction.refund('transaction_id')


Transaction Flow Sequence Example 2
-----------------------------------

#. Authorization Only
#. Get Details (recommended for shipping)
#. Authorization Only, Continue
#. Void

.. code-block:: python

    result = authorize.Transaction.auth({
        'amount': 40.00,
        'pay_pal': {
            'success_url': 'https://my.server.com/success.html',
            'cancel_url': 'https://my.server.com/cancel.html',
            'locale': 'US',
            'header_image': 'https://usa.visa.com/img/home/logo_visa.gif',
            'flow_color': 'FF0000'
        },
    })

    result.transaction_response.trans_id
    # e.g. 'transaction_id'

    result.secure_acceptance.secure_acceptance_url
    # e.g. https://www.paypal.com/cgibin/webscr?cmd=_express-checkout&token=EC-4WL17777V4111184H

    # (optional) get shipping information for order
    details = authorize.Transaction.details('transaction_id')

    authorize.Transaction.auth_continue('transaction_id', 'payer_id')

    authorize.Transaction.void('transaction_id')


Transaction Flow Sequence Example 3
-----------------------------------

#. Authorization and Capture
#. Get Details (recommended for shipping)
#. Authorization and Capture, Continue
#. Refund (optional)

.. code-block:: python

    result = authorize.Transaction.sale({
        'amount': 40.00,
        'pay_pal': {
            'success_url': 'https://my.server.com/success.html',
            'cancel_url': 'https://my.server.com/cancel.html',
            'locale': 'US',
            'header_image': 'https://usa.visa.com/img/home/logo_visa.gif',
            'flow_color': 'FF0000'
        },
    })

    result.transaction_response.trans_id
    # e.g. 'transaction_id'

    result.secure_acceptance.secure_acceptance_url
    # e.g. https://www.paypal.com/cgibin/webscr?cmd=_express-checkout&token=EC-4WL17777V4111184H

    # (optional) get shipping information for order
    details = authorize.Transaction.details('transaction_id')

    authorize.Transaction.sale_continue('transaction_id', 'payer_id')

    authorize.Transaction.refund('transaction_id')

