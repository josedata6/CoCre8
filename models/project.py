from models.base_model import BaseModel

class Project(BaseModel):
    def create(self, title, description, created_by):
        """Create a new project."""
        self._run(
            "INSERT INTO Projects (title, description, created_by) VALUES (?, ?, ?)",
            (title, description, created_by)
        )
#        # This line checks if the created_by user exists in the Users table.
    def getById(self, project_id):
        """Get project details by ID."""
        rows = self._run("SELECT * FROM Projects WHERE project_id = ?", (project_id,), fetch=True)
        return rows[0] if rows else None

    def update(self, project_id, title=None, description=None):
        """Update project details."""
        fields, values = [], []
        if title:
            fields.append("title = ?")
            values.append(title)
        if description:
            fields.append("description = ?")
            values.append(description)
        values.append(project_id)
        sql = f"UPDATE Projects SET {', '.join(fields)} WHERE project_id = ?"
        self._run(sql, tuple(values))

    def delete(self, project_id):
        """Delete a project."""
        self._run("DELETE FROM Projects WHERE project_id = ?", (project_id,))

    def listAll(self):
        """List all projects."""
        return self._run("SELECT * FROM Projects", fetch=True)
