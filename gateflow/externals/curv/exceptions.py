class CurvRequestException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return 'CurvRequestException: %s' % self.message