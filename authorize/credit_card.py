from authorize import Configuration


class CreditCard(object):

    @staticmethod
    def create(customer_id, params={}):
        return Configuration.api.credit_card.create(customer_id, params)

    @staticmethod
    def details(customer_id, payment_id):
        return Configuration.api.credit_card.details(customer_id, payment_id)

    @staticmethod
    def update(customer_id, payment_id, params={}):
        return Configuration.api.credit_card.update(customer_id, payment_id, params)

    @staticmethod
    def delete(customer_id, payment_id):
        return Configuration.api.credit_card.delete(customer_id, payment_id)

    @staticmethod
    def validate(customer_id, payment_id, params={}):
        return Configuration.api.credit_card.validate(customer_id, payment_id, params)
