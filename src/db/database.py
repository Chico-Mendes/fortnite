import sqlite3

from db.repositories.sprite_repository import SpriteRepository

DB_PATH = "db/database.db"


class Database:
    def __init__(self):
        """Get a connection to the SQLite database."""
        conn = sqlite3.connect(DB_PATH)
        conn.row_factory = sqlite3.Row
        # Enable foreign key support
        conn.execute("PRAGMA foreign_keys = ON")

        self.sprites = SpriteRepository(conn)
