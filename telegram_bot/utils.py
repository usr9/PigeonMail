import psycopg2
from psycopg2.extras import RealDictCursor

import config
import logging

logging.basicConfig(
    format="%(asctime)s - %(name)s:%(lineno)d - %(levelname)s - %(message)s", level=logging.INFO
)

logger = logging.getLogger(__name__)


def get_db_connection():
    try:
        connection = psycopg2.connect(
            dbname=config.DB_CONFIG["dbname"],
            user=config.DB_CONFIG["user"],
            password=config.DB_CONFIG["password"],
            host=config.DB_CONFIG["host"],
            port=config.DB_CONFIG["port"],
            cursor_factory=RealDictCursor
        )
        # Check connection
        connection.cursor().execute("SELECT 1")
        return connection
    except psycopg2.OperationalError as e:
        logging.error(f"Database connection failed: {e}")
        raise


def register_user(chat_id, username, db_conn: psycopg2.extensions.connection) -> None:
    cursor = db_conn.cursor()
    cursor.execute(
        "INSERT INTO users (tg_user_id, username) VALUES (%s, %s) ON CONFLICT DO NOTHING",
        (chat_id, username)
    )
    db_conn.commit()
    

def insert_message(sender_id, recipient_id, message, db_conn: psycopg2.extensions.connection) -> None:
    cursor = db_conn.cursor()
    cursor.execute(
        "INSERT INTO messages (sender_id, recipient_id, message) VALUES (%s, %s, %s)",
        (sender_id, recipient_id, message)
    )
    db_conn.commit()

def get_all_users(db_conn: psycopg2.extensions.connection) -> list:
    cursor = db_conn.cursor()
    cursor.execute("SELECT username FROM users")
    return cursor.fetchall()

def insert_location(user_id, latitude, longitude, db_conn: psycopg2.extensions.connection) -> None:
    cursor = db_conn.cursor()
    cursor.execute(
        "INSERT INTO user_locations (tg_user_id, latitude, longitude) VALUES (%s, %s, %s) ON CONFLICT (tg_user_id) DO NOTHING",
        (user_id, latitude, longitude)
    )
    db_conn.commit()