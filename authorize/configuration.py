from authorize.apis.authorize_api import AuthorizeAPI


class Configuration(object):

    @staticmethod
    def configure(environment, login_id, transaction_key):
        Configuration.environment = environment
        Configuration.login_id = login_id
        Configuration.transaction_key = transaction_key
        Configuration.api = AuthorizeAPI(Configuration.instantiate())

    @staticmethod
    def instantiate():
        return Configuration(
            Configuration.environment,
            Configuration.login_id,
            Configuration.transaction_key,
        )

    def __init__(self, environment, login_id, transaction_key):
        self.environment = environment
        self.login_id = login_id
        self.transaction_key = transaction_key
