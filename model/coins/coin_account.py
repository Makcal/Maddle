class CoinAccount:
    def __init__(self, id, token):
        self.id = id
        self.token = token

    def __iter__(self):
        yield self.id
        yield self.token
