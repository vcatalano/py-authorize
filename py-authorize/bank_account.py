from authorize import Configuration


class BankAccount(object):

    @staticmethod
    def create(customer_id, params={}):
        return Configuration.api.bank_account.create(customer_id, params)

    @staticmethod
    def details(customer_id, payment_id):
        return Configuration.api.bank_account.details(customer_id, payment_id)

    @staticmethod
    def update(customer_id, payment_id, params={}):
        return Configuration.api.bank_account.update(customer_id, payment_id, params)

    @staticmethod
    def delete(customer_id, payment_id):
        return Configuration.api.bank_account.delete(customer_id, payment_id)
