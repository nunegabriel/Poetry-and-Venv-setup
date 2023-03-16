import psycopg2
from pathlib import Path
from dotenv import load_dotenv
import os

env_path = Path('.', '.env')
load_dotenv(dotenv_path=env_path)

db_name = os.getenv("DATABASE_NAME")
db_user = os.getenv("DATABASE_USER")
db_password = os.getenv("DATABASE_PASSWORD")
db_host = "localhost"
db_port = "5432"

def get_db():
    """
    Open a new database connection and return a cursor object.
    """
    conn = psycopg2.connect(
        dbname=db_name,
        user=db_user,
        password=db_password,
        host=db_host,
        port=db_port
    )
    cursor = conn.cursor()
    return cursor

