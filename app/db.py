import psycopg2
from psycopg2.extras import RealDictCursor
import os

def get_connection():
    DATABASE_URL = os.getenv("DATABASE_URL")  # URL do PostgreSQL no Render
    conn = psycopg2.connect(DATABASE_URL, cursor_factory=RealDictCursor)
    return conn
