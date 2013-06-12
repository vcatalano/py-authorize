from authorize.configuration import Configuration
from authorize.environment import Environment


def setUpPackage():
    Configuration.configure(
        Environment.TEST,
        '8s8tVnG5t',
        '5GK7mncw8mG2946z',
    )
