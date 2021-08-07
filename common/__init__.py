from json import load
import os
import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import registry, sessionmaker


with open(os.path.join('common', 'data.json')) as file:
    data: dict = load(file)
    DB_PROTOCOL = data['db_dialect_with_driver']
    DB_USERNAME = data['db_username']
    DB_PASSWORD = data['db_password']
    DB_LOCATION = data['db_location']
    DB_NAME = data['db_name']

    VK_ID = data['vk_id']
    VK_TOKEN = data['vk_token']
    GROUP_TOKEN = data['group_token']
    APP_KEY = data['app_key']
    BOT_SECRET = data['bot_secret']

    VKCOIN_KEY = data['vkcoin_key']
    BYTECOIN_TOKEN = data['bytecoin_token']
    PS_ID = data['ps_id']
    PS_TOKEN = data['ps_token']
    PS_SECRET = data['ps_secret']
    CORONA_TOKEN = data['corona_token']
    VKPOINT_TOKEN = data['vkpoint_token']
    CATCOIN_TOKEN = data['catcoin_token']
    WORLDCOIN_ID = data['worldcoin_id']
    WORLDCOIN_TOKEN = data['worldcoin_token']

if sys.platform.startswith('win'):
    DB_USERNAME = 'root'
    DB_PASSWORD = '12356790d'
    DB_LOCATION = 'localhost:3306'

engine = create_engine(f'{DB_PROTOCOL}://'
                       f'{DB_USERNAME}:{DB_PASSWORD}@'
                       f'{DB_LOCATION}/{DB_NAME}',
                       echo=True,
                       future=True)
get_session = sessionmaker(engine)

registry = registry(_bind=engine)
Model = registry.generate_base(name='Model')

# __all__ = ['engine', 'get_session', 'registry', 'Model']
