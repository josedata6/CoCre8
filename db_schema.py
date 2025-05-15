import sqlite3  # Import the SQLite module to interact with the local database

# Dictionary-driven table definitions for the Co-Cre8 app
# Each key is a table name, and each value is a dictionary of column definitions
TABLE_DEFS = {
    "Users": {
        "user_id": "INTEGER PRIMARY KEY AUTOINCREMENT",  # Unique user ID
        "name": "TEXT NOT NULL",                         # User's name
        "email": "TEXT NOT NULL UNIQUE",                 # Unique email address
        "bio": "TEXT"                                    # Short user biography
    },
    "Projects": {
        "project_id": "INTEGER PRIMARY KEY AUTOINCREMENT",  # Unique project ID
        "title": "TEXT NOT NULL",                           # Project title
        "description": "TEXT",                              # Project description
        "created_by": "INTEGER NOT NULL",                   # FK to Users table
        "FOREIGN KEY(created_by)": "REFERENCES Users(user_id)"  # Enforce FK
    },
    "Membership": {
        "user_id": "INTEGER",                                # FK to Users table
        "project_id": "INTEGER",                             # FK to Projects table
        "role": "TEXT",                                      # Role in the project
        "join_date": "TEXT",                                 # Join date (YYYY-MM-DD)
        "PRIMARY KEY(user_id, project_id)": "",              # Composite primary key
        "FOREIGN KEY(user_id)": "REFERENCES Users(user_id)", # Enforce FK
        "FOREIGN KEY(project_id)": "REFERENCES Projects(project_id)"
    },
    "Skills": {
        "skill_id": "INTEGER PRIMARY KEY AUTOINCREMENT",     # Unique skill ID
        "skill_name": "TEXT NOT NULL UNIQUE"                 # Name of the skill
    },
    "ProjectSkills": {
        "project_id": "INTEGER",                             # FK to Projects table
        "skill_id": "INTEGER",                               # FK to Skills table
        "PRIMARY KEY(project_id, skill_id)": "",             # Composite primary key
        "FOREIGN KEY(project_id)": "REFERENCES Projects(project_id)",
        "FOREIGN KEY(skill_id)": "REFERENCES Skills(skill_id)"
    },
    "Messages": {
        "message_id": "INTEGER PRIMARY KEY AUTOINCREMENT",   # Unique message ID
        "sender_id": "INTEGER NOT NULL",                     # FK to Users table
        "project_id": "INTEGER NOT NULL",                    # FK to Projects table
        "content": "TEXT",                                   # Message content
        "sent_at": "TEXT",                                   # Timestamp (as string)
        "FOREIGN KEY(sender_id)": "REFERENCES Users(user_id)",
        "FOREIGN KEY(project_id)": "REFERENCES Projects(project_id)"
    }
}

def initDb(db_path="projectmatch.db"):
    """
    Initializes the SQLite database using the TABLE_DEFS dictionary.
    Creates tables if they do not already exist.
    """
    conn = sqlite3.connect(db_path)   # Connect to (or create) the SQLite database
    cur = conn.cursor()               # Create a cursor to execute SQL statements

    # Loop through each table definition
    for table, fields in TABLE_DEFS.items():
        # Extract standard column definitions (skip foreign keys)
        columns = ",\n    ".join([
            f"{col} {typ}" for col, typ in fields.items() if not col.startswith("FOREIGN KEY")
        ])

        # Extract foreign key constraints, if any
        fks = ",\n    ".join([
            f"{col} {typ}" for col, typ in fields.items() if col.startswith("FOREIGN KEY")
        ])

        # Construct the SQL CREATE TABLE statement
        ddl = f"CREATE TABLE IF NOT EXISTS {table} (\n    {columns}" + (
            f",\n    {fks}" if fks else ""
        ) + "\n);"

        cur.execute(ddl)  # Execute the SQL statement to create the table

    conn.commit()  # Save changes to the database
    conn.close()   # Close the connection

# Run the initDb function only if this file is executed directly
if __name__ == "__main__":
    initDb()
