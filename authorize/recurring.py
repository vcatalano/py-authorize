from authorize import Configuration


class Recurring(object):

    @staticmethod
    def create(params={}):
        return Configuration.api.recurring.create(params)

    @staticmethod
    def details(subscription_id, full=False):
        return Configuration.api.recurring.details(subscription_id, full)

    @staticmethod
    def update(subscription_id, params={}):
        return Configuration.api.recurring.update(subscription_id, params)

    @staticmethod
    def delete(subscription_id):
        return Configuration.api.recurring.delete(subscription_id)

    @staticmethod
    def list(params={}):
        return Configuration.api.recurring.list(params)
