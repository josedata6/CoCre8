from models.base_model import BaseModel

class Message(BaseModel):
    def create(self, sender_id, project_id, content, sent_at):
        """Create a message tied to a project and sender."""
        self._run(
            "INSERT INTO Messages (sender_id, project_id, content, sent_at) VALUES (?, ?, ?, ?)",
            (sender_id, project_id, content, sent_at)
        )

    def getById(self, message_id):
        """Retrieve a message by its ID."""
        rows = self._run(
            "SELECT * FROM Messages WHERE message_id = ?",
            (message_id,),
            fetch=True
        )
        return rows[0] if rows else None

    def update(self, message_id, content):
        """Update the content of a message."""
        self._run("UPDATE Messages SET content = ? WHERE message_id = ?", (content, message_id))

    def delete(self, message_id):
        """Delete a message by ID."""
        self._run("DELETE FROM Messages WHERE message_id = ?", (message_id,))

    def listAll(self):
        """List all messages."""
        return self._run("SELECT * FROM Messages", fetch=True)
