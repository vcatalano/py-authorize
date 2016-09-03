Batch
=====

Transactions are batched and sent for settlement on a daily basis. 
Py-Authorize provides basic batch methods based on Authorize.net's 
reporting API.

List
----

The `list` method returns the batch ID, Settlement Time and other batch 
statistics for all settled batches within a range of dates.

.. code-block:: python

    result = authorize.Batch.list({
        'start': '2012-01-01',
        'end': '2012-05-31',
    })


If the `start` and `end` dates are not specified, the `list` method will 
return the batches processed in the past 24 hours.

.. code-block:: python

    result = authorize.Batch.list()


Details
-------

The `details` method returns batch statistics for a given batch ID.

.. code-block:: python

    result = authorize.Batch.details('2552096')

