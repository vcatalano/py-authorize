import datetime

from authorize import Configuration
from authorize.xml_data import prettify

from unittest import TestCase

LIST_BATCH_DATES = {
    'start': datetime.datetime(2012, 5, 1), #'2012-05-01T00:00:00'
    'end': datetime.datetime(2012, 5, 31), #'2012-05-31T00:00:00'
}

BATCH_DETAILS_REQUEST = '''
<?xml version="1.0" ?>
<getBatchStatisticsRequest xmlns="AnetApi/xml/v1/schema/AnetApiSchema.xsd">
  <merchantAuthentication>
    <name>8s8tVnG5t</name>
    <transactionKey>5GK7mncw8mG2946z</transactionKey>
  </merchantAuthentication>
  <batchId>879802352356</batchId>
</getBatchStatisticsRequest>
'''

LIST_BATCH_REQUEST = '''
<?xml version="1.0" ?>
<getSettledBatchListRequest xmlns="AnetApi/xml/v1/schema/AnetApiSchema.xsd">
  <merchantAuthentication>
    <name>8s8tVnG5t</name>
    <transactionKey>5GK7mncw8mG2946z</transactionKey>
  </merchantAuthentication>
  <includeStatistics>true</includeStatistics>
  <firstSettlementDate>2012-05-01T00:00:00</firstSettlementDate>
  <lastSettlementDate>2012-05-31T00:00:00</lastSettlementDate>
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
