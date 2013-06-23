from colander import Invalid


class AuthorizeError(Exception):

    """Base class for connection and response errors."""


class AuthorizeConnectionError(AuthorizeError):

    """Error communicating with the Authorize.net API."""


class AuthorizeResponseError(AuthorizeError):

    """Error response code returned from API."""


class AuthorizeInvalidError(AuthorizeError, Invalid):

    def __init__(self, invalid):
        self.node = invalid.node
        self.msg = invalid.msg
        self.value = invalid.value
        self.children = invalid.children
