from authorize import Configuration


class Batch(object):

    @staticmethod
    def details(batch_id):
        return Configuration.api.batch.details(batch_id)

    @staticmethod
    def list(params={}):
        return Configuration.api.batch.list(params)
