import sqlite3

class BaseModel:
    def __init__(self, db_path="projectmatch.db"):
        self.db_path = db_path

    def _run(self, query, params=(), fetch=False):
        """Executes a query with optional parameters. Set fetch=True to retrieve results."""
        with sqlite3.connect(self.db_path) as conn:
            cur = conn.cursor()
            cur.execute(query, params)
            if fetch:
                return cur.fetchall()
            conn.commit()
            return cur
