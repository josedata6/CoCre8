import sqlite3

# Dictionary-driven table definitions
TABLE_DEFS = {
    "Users": {
        "user_id": "INTEGER PRIMARY KEY AUTOINCREMENT",
        "name": "TEXT NOT NULL",
        "email": "TEXT NOT NULL UNIQUE",
        "bio": "TEXT"
    },
    "Projects": {
        "project_id": "INTEGER PRIMARY KEY AUTOINCREMENT",
        "title": "TEXT NOT NULL",
        "description": "TEXT",
        "created_by": "INTEGER NOT NULL",
        "FOREIGN KEY(created_by)": "REFERENCES Users(user_id)"
    },
    "Membership": {
        "user_id": "INTEGER",
        "project_id": "INTEGER",
        "role": "TEXT",
        "join_date": "TEXT",
        "PRIMARY KEY(user_id, project_id)": "",
        "FOREIGN KEY(user_id)": "REFERENCES Users(user_id)",
        "FOREIGN KEY(project_id)": "REFERENCES Projects(project_id)"
    },
    "Skills": {
        "skill_id": "INTEGER PRIMARY KEY AUTOINCREMENT",
        "skill_name": "TEXT NOT NULL UNIQUE"
    },
    "ProjectSkills": {
        "project_id": "INTEGER",
        "skill_id": "INTEGER",
        "PRIMARY KEY(project_id, skill_id)": "",
        "FOREIGN KEY(project_id)": "REFERENCES Projects(project_id)",
        "FOREIGN KEY(skill_id)": "REFERENCES Skills(skill_id)"
    },
    "Messages": {
        "message_id": "INTEGER PRIMARY KEY AUTOINCREMENT",
        "sender_id": "INTEGER NOT NULL",
        "project_id": "INTEGER NOT NULL",
        "content": "TEXT",
        "sent_at": "TEXT",
        "FOREIGN KEY(sender_id)": "REFERENCES Users(user_id)",
        "FOREIGN KEY(project_id)": "REFERENCES Projects(project_id)"
    }
}

def initDb(db_path="projectmatch.db"):
    """Initializes the SQLite database using the TABLE_DEFS dictionary."""
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    for table, fields in TABLE_DEFS.items():
        columns = ",\n    ".join([
            f"{col} {typ}" for col, typ in fields.items() if not col.startswith("FOREIGN KEY")
        ])
        fks = ",\n    ".join([
            f"{col} {typ}" for col, typ in fields.items() if col.startswith("FOREIGN KEY")
        ])
        ddl = f"CREATE TABLE IF NOT EXISTS {table} (\n    {columns}" + (
            f",\n    {fks}" if fks else ""
        ) + "\n);"
        cur.execute(ddl)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    initDb()
