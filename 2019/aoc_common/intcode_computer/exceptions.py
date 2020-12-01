

class RanOut(BaseException):
    pass


class UnknownOpCode(BaseException):
    pass


class UnknownParameterMode(BaseException):
    pass


class Finished(BaseException):
    pass


class WaitingForInput(BaseException):
    pass


class NotExpectingInput(BaseException):
    pass


class WaitingForOutput(BaseException):
    pass


class NotExpectingOutput(BaseException):
    pass

