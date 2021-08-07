async def fetch_users(users, api, session, **params):
    params.update(api._method_default_args)  # noqa
    params["user_ids"] = ", ".join(map(str, users))
    params["access_token"] = api._session.access_token  # noqa

    async with session.post("https://api.vk.com/method/users.get",
                            data=params) as response:
        return (await response.json())['response']
