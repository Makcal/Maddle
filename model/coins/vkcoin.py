from json import loads
from random import randint
import aiohttp
import asyncio

from vkcoin import VKCoin as VKCoin_

from .coin import Coin
from .coin_account import CoinAccount
from common import VK_ID, VKCOIN_KEY
from util.async_tasks import run_by_chunks


class VKCoin(Coin):
    @staticmethod
    def get_name():
        return 'vkcoin'

    def init_account(self) -> CoinAccount:
        return CoinAccount(VK_ID, VKCOIN_KEY)

    async def _fetch_users(self, users):
        params = {
            'merchantId': self.account.id,
            'key': self.account.token,
            'userIds': users
        }

        async with aiohttp.ClientSession() as session:
            async with session.post(
                    'https://coin-without-bugs.vkforms.ru/merchant/score',
                    json=params
            ) as response:
                return {int(k): v / 1000
                        for k, v
                        in loads(await response.text())['response'].items()}

    def get_accounts_data(self, *ids):
        if not ids:
            return {}

        total = {}
        for dict_ in asyncio.run(run_by_chunks(self._fetch_users, ids, 100)):
            total.update(dict_)
        return total

    def get_payment_url(self, amount, to_id=None, free_amount=False):
        user_id = to_id if to_id is not None else self.account.id
        return VKCoin_(user_id, None).get_payment_url(
            amount,
            payload=randint(-2 * 10**9, 2 * 10**9),
            free_amount=free_amount
        )

    def send_money(self, to_id, amount, as_merchant=True):
        return VKCoin_(*self.account).send_payment(to_id, amount, as_merchant)

    def get_transactions(self, count=None, offset=0, last=None, ids=None):
        """
        ids: [1] returns transactions from payment links.
             [2] returns incoming and
        """
        if not ids:
            ids = [1]

        result = VKCoin_(*self.account).get_transactions(ids, last_tx=last)
        if count is None:
            result = result[offset:]
        else:
            result = result[offset:offset+count]
        return result
