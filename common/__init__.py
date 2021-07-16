from json import load
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import registry, sessionmaker

with open(os.path.join("common", "data.json")) as file:
    data: dict = load(file)
    DB_PROTOCOL = data["db_dialect_with_driver"]
    DB_USERNAME = data["db_username"]
    DB_PASSWORD = data["db_password"]
    DB_LOCATION = data["db_location"]
    DB_NAME = data["db_name"]

if os.name == "nt":
    DB_USERNAME = "root"
    DB_PASSWORD = "12356790d"
    DB_LOCATION = "localhost:3306"

engine = create_engine(f"{DB_PROTOCOL}://"
                       f"{DB_USERNAME}:{DB_PASSWORD}@"
                       f"{DB_LOCATION}/{DB_NAME}",
                       echo=True,
                       future=True)
get_session = sessionmaker(engine)

registry = registry(_bind=engine)
Model = registry.generate_base(name="Model")

__all__ = ['engine', 'get_session', 'registry', 'Model']
