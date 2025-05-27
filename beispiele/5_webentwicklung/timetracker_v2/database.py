from dataclasses import dataclass
import sqlite3


@dataclass
class Activity:
    id: int | None  # None when not yet stored in DB
    description: str
    start_time: str
    end_time: str
    tags: str


class ActivityDB:
    def __init__(self, db_path="activities.db"):
        self.db_path = db_path
        self._init_db()

    @property
    def conn(self):
        return sqlite3.connect(self.db_path)

    def _init_db(self):
        with self.conn as cnx:
            c = cnx.cursor()
            c.execute("""
                CREATE TABLE IF NOT EXISTS activities (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    description TEXT NOT NULL,
                    start_time TEXT NOT NULL,
                    end_time TEXT,
                    tags TEXT
                )
            """)
            self.conn.commit()

    def get_activities(self):
        with self.conn as cnx:
            c = cnx.cursor()
            c.execute("""
                SELECT id, description, start_time, end_time, tags
                FROM activities
                ORDER BY start_time DESC
            """)
            rows = c.fetchall()
            return [Activity(*row) for row in rows]

    def store_activity(self, activity: Activity) -> int:
        with self.conn as cnx:
            c = cnx.cursor()
            c.execute("""
                INSERT INTO activities (description, start_time, end_time, tags)
                VALUES (?, ?, ?, ?)
                """,
                (activity.description, activity.start_time, activity.end_time, activity.tags),
            )
            activity_id = c.lastrowid
            self.conn.commit()

        return activity_id

    def get_activity(self, activity_id: int) -> Activity | None:
        with self.conn as cnx:
            c = cnx.cursor()
            c.execute(
                "SELECT id, description, start_time, end_time, tags FROM activities WHERE id = ?",
                (activity_id,),
            )
            row = c.fetchone()

        if row:
            return Activity(*row)
        return None

    def delete_activity(self, activity_id: int):
        with self.conn as cnx:
            c = cnx.cursor()
            c.execute("DELETE FROM activities WHERE id = ?", (activity_id,))
            self.conn.commit()

    def end_activity(self, activity_id: int, end_time: str):
        with self.conn as cnx:
            c = cnx.cursor()
            c.execute("""
                UPDATE activities
                SET end_time = ?
                WHERE id = ?
                """,
                (end_time, activity_id)
            )
            self.conn.commit()
