from authorize import Batch
from authorize import AuthorizeResponseError

from nose.plugins.attrib import attr

from unittest2 import TestCase

LIST_BATCH_DATES = {
    'start': '2012-01-01',
    'end': '2012-05-31',
}

LIST_BATCH_DATES_START_ONLY = {
    'start': '2012-01-01',
}


@attr('live_tests')
class BatchTests(TestCase):

    def test_batch_details(self):
        Batch.details('2520288')
        self.assertRaises(AuthorizeResponseError, Batch.details, 'Bad batch ID')

    def test_list_batch(self):
        Batch.list()
        Batch.list(LIST_BATCH_DATES)
        Batch.list(LIST_BATCH_DATES_START_ONLY)
