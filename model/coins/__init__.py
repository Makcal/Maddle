from .coin import Coin
from .vkcoin import VKCoin

coin_list = [VKCoin]
COIN_CLASSES = {c.query_id(): c for c in coin_list}

__all__ = ['coin_list', 'Coin', 'VKCoin', 'COIN_CLASSES']
