class MaddleError(Exception):
    def __init__(self, code, *args):
        super(MaddleError, self).__init__(*args)
        self.code = code


class MissingParameterError(MaddleError, TypeError):
    def __init__(self, params):
        super(MissingParameterError, self).__init__(
            1,
            f"These parameters are missing: " + ', '.join(params)
        )


class WrongParameterValueError(MaddleError, ValueError):
    def __init__(self, values):
        super(WrongParameterValueError, self).__init__(
            2,
            f"These parameters have wrong value: " + ', '.join(
                '{%s: %r}' % (k, v)
                for k, v
                in values.items()
            )
        )


class UnknownUserError(MaddleError):
    def __init__(self, user_id):
        super(UnknownUserError, self).__init__(
            3,
            f"User {user_id} doesn't exist"
        )


class UnknownCurrencyError(MaddleError):
    def __init__(self, currency_name):
        super(UnknownCurrencyError, self).__init__(
            4,
            f"Currency {currency_name} doesn't exist"
        )


class NotEnoughMoneyError(MaddleError):
    def __init__(self, user_id, currency_name):
        super(NotEnoughMoneyError, self).__init__(
            5,
            f"User id{user_id} has not enough {currency_name}"
        )


class EmptyBankAccountError(MaddleError):
    def __init__(self, user_id):
        super(EmptyBankAccountError, self).__init__(
            6,
            f"User id{user_id} has no money on account to withdraw"
        )
