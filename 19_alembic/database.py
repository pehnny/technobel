import os, dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

dotenv.load_dotenv()
_db_url = os.getenv("DB_URL")
if _db_url == None:
    raise ValueError()

_engine = create_engine(_db_url, echo=False)
session = sessionmaker(_engine)