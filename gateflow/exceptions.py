class BaseGateFlowException(Exception):
    """
    Base exception class for this module
    """
    pass

class InputException(BaseGateFlowException):
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message