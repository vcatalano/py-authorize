from authorize import Configuration
from authorize.xml_data import prettify

from unittest2 import TestCase

LIST_BATCH_DATES = {
    'start': '2012-01-01T16:00:00Z',
    'end': '2012-05-31T16:00:00Z',
}

BATCH_DETAILS_REQUEST = u'''
<?xml version="1.0" ?>
<getBatchStatisticsRequest xmlns="AnetApi/xml/v1/schema/AnetApiSchema.xsd">
  <merchantAuthentication>
    <name>8s8tVnG5t</name>
    <transactionKey>5GK7mncw8mG2946z</transactionKey>
  </merchantAuthentication>
  <batchId>879802352356</batchId>
</getBatchStatisticsRequest>
'''

LIST_BATCH_REQUEST = u'''
<?xml version="1.0" ?>
<getSettledBatchListRequest xmlns="AnetApi/xml/v1/schema/AnetApiSchema.xsd">
  <merchantAuthentication>
    <name>8s8tVnG5t</name>
    <transactionKey>5GK7mncw8mG2946z</transactionKey>
  </merchantAuthentication>
  <includeStatistics>true</includeStatistics>
  <firstSettlementDate>2012-01-01T16:00:00Z</firstSettlementDate>
  <lastSettlementDate>2012-05-31T16:00:00Z</lastSettlementDate>
</getSettledBatchListRequest>
'''


class BatchAPITests(TestCase):

    maxDiff = None

    def test_batch_details_request(self):
        request_xml = Configuration.api.batch._details_request('879802352356')
        request_string = prettify(request_xml)
        self.assertEqual(request_string, BATCH_DETAILS_REQUEST.strip())

    def test_list_batch_request(self):
        request_xml = Configuration.api.batch._list_request(LIST_BATCH_DATES)
        request_string = prettify(request_xml)
        self.assertEqual(request_string, LIST_BATCH_REQUEST.strip())
