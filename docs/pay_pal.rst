PayPal Express Checkout
=======================

Authorize.net now provides functionality for PayPal Express Checkout. With
PayPal Express Checkout, you can accept payments with PayPal while utilizing
Authorize.net's reporting functionality.

Transaction Flow Sequence Example 1
-----------------------------------

The following authorization...

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
    # e.g. '2194343352'

    result.secure_acceptance.secure_acceptance_url
    # e.g. https://www.paypal.com/cgibin/webscr?cmd=_express-checkout&token=EC-4WL17777V4111184H

    # (optional) get shipping information for order
    details = authorize.Transaction.details('2194343352')

    authorize.Transaction.auth_continue('2194343352', '7E7MGXCWTTKK2')

    authorize.Transaction.settle('2194343352')

    # (optional) refund the transaction
    authorize.Transaction.refund('2194343352')


Transaction Flow Sequence Example 2
-----------------------------------

The following authorization...

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
    # e.g. '2194343352'

    result.secure_acceptance.secure_acceptance_url
    # e.g. https://www.paypal.com/cgibin/webscr?cmd=_express-checkout&token=EC-4WL17777V4111184H

    # (optional) get shipping information for order
    details = authorize.Transaction.details('2194343352')

    authorize.Transaction.auth_continue('2194343352', '7E7MGXCWTTKK2')

    authorize.Transaction.void('2194343352')


Transaction Flow Sequence Example 3
-----------------------------------

The following authorization...

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
    # e.g. '2194343352'

    result.secure_acceptance.secure_acceptance_url
    # e.g. https://www.paypal.com/cgibin/webscr?cmd=_express-checkout&token=EC-4WL17777V4111184H

    # (optional) get shipping information for order
    details = authorize.Transaction.details('2194343352')

    authorize.Transaction.auth_continue('2194343352', '7E7MGXCWTTKK2')

    authorize.Transaction.settle('2194343352')

