import colander

from authorize.exceptions import AuthorizeInvalidError


class BaseAPI(object):

    def __init__(self, api):
        self.api = api
        self.config = api.config

    def _deserialize(self, schema, params={}):
        try:
            deserialized = schema.deserialize(params)
        except colander.Invalid as e:
            raise AuthorizeInvalidError(e)
        return deserialized
