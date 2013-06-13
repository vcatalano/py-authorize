from authorize import Configuration


class Address(object):

    @staticmethod
    def create(customer_id, params={}):
        return Configuration.api.address.create(customer_id, params)

    @staticmethod
    def details(customer_id, address_id):
        return Configuration.api.address.details(customer_id, address_id)

    @staticmethod
    def update(customer_id, address_id, params={}):
        return Configuration.api.address.update(customer_id, address_id, params)

    @staticmethod
    def delete(customer_id, address_id):
        return Configuration.api.address.delete(customer_id, address_id)
