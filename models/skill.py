from models.base_model import BaseModel

class Skill(BaseModel):
    def create(self, skill_name):
        """Add a new skill to the Skills table."""
        self._run("INSERT INTO Skills (skill_name) VALUES (?)", (skill_name,))

    def getById(self, skill_id):
        """Retrieve a skill by its ID."""
        rows = self._run("SELECT * FROM Skills WHERE skill_id = ?", (skill_id,), fetch=True)
        return rows[0] if rows else None

    def update(self, skill_id, skill_name):
        """Update the name of a skill."""
        self._run("UPDATE Skills SET skill_name = ? WHERE skill_id = ?", (skill_name, skill_id))

    def delete(self, skill_id):
        """Delete a skill by its ID."""
        self._run("DELETE FROM Skills WHERE skill_id = ?", (skill_id,))

    def listAll(self):
        """List all skills in the database."""
        return self._run("SELECT * FROM Skills", fetch=True)
