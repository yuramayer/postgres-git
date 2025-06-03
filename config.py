"""Loading environment vars to the project"""

import os
from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_PORT = int(os.getenv("DB_PORT"))
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

RES_DIR = 'postgres_db'

SCHEMAS = ('dwh', 'dwh_vitr', 'dwh_view', 'dwh_vitr_view')
