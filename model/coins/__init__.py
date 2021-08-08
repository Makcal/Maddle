from .coin import Coin
from .vkcoin import VKCoin

_coins = [VKCoin]
COIN_CLASSES = {c.get_name(): c for c in _coins}

__all__ = ['Coin', 'VKCoin', 'COIN_CLASSES']
