from sqlite3 import Connection
from typing import List

from db.models import Sprite


class SpriteRepository:
    def __init__(self, conn: Connection):
        self.conn: Connection = conn

    def create(self, sprite: Sprite) -> None:
        """Insert a new sprite into the database."""
        self.conn.execute(
            "INSERT INTO sprites (code, name) VALUES (?, ?)",
            (sprite.code, sprite.name),
        )
        self.conn.commit()

    def get_all(self) -> List[Sprite]:
        """Retrieve all sprites from the database."""
        rows = self.conn.execute("SELECT code, name FROM sprites").fetchall()
        return [Sprite(code=row[0], name=row[1]) for row in rows]
