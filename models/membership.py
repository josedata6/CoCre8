from models.base_model import BaseModel

class Membership(BaseModel):
    def create(self, user_id, project_id, role, join_date):
        """Add a user to a project with a role and join date."""
        self._run(
            "INSERT INTO Membership (user_id, project_id, role, join_date) VALUES (?, ?, ?, ?)",
            (user_id, project_id, role, join_date)
        )

    def getById(self, user_id, project_id):
        """Retrieve a membership record by user and project ID."""
        rows = self._run(
            "SELECT * FROM Membership WHERE user_id = ? AND project_id = ?",
            (user_id, project_id),
            fetch=True
        )
        return rows[0] if rows else None

    def update(self, user_id, project_id, role=None, join_date=None):
        """Update role or join date of a project membership."""
        fields, values = [], []
        if role:
            fields.append("role = ?")
            values.append(role)
        if join_date:
            fields.append("join_date = ?")
            values.append(join_date)
        values.extend([user_id, project_id])
        sql = f"UPDATE Membership SET {', '.join(fields)} WHERE user_id = ? AND project_id = ?"
        self._run(sql, tuple(values))

    def delete(self, user_id, project_id):
        """Remove a user from a project."""
        self._run("DELETE FROM Membership WHERE user_id = ? AND project_id = ?", (user_id, project_id))

    def listAll(self):
        """List all membership records."""
        return self._run("SELECT * FROM Membership", fetch=True)
