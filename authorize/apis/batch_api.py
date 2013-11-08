import xml.etree.cElementTree as E

from authorize.apis.base_api import BaseAPI
from authorize.schemas import ListBatchSchema
from authorize.xml_data import *


class BatchAPI(BaseAPI):

    def details(self, batch_id):
        return self.api._make_call(self._details_request(batch_id))

    def list(self, params={}):
        batch = self._deserialize(ListBatchSchema(), params)
        return self.api._make_call(self._list_request(batch))

    # The following methods generate the XML for the corresponding API calls.
    # This makes unit testing each of the calls easier.
    def _details_request(self, batch_id):
        request = self.api._base_request('getBatchStatisticsRequest')
        E.SubElement(request, 'batchId').text = batch_id
        return request

    def _list_request(self, params={}):
        request = self.api._base_request('getSettledBatchListRequest')
        E.SubElement(request, 'includeStatistics').text = 'true'
        if 'start' in params:
            E.SubElement(request, 'firstSettlementDate').text = params['start'].strftime('%Y-%m-%dT%H:%M:%S')
        if 'end' in params:
            E.SubElement(request, 'lastSettlementDate').text = params['end'].strftime('%Y-%m-%dT%H:%M:%S')
        return request
