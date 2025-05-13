from models.base_model import BaseModel

class ProjectSkill(BaseModel):
    def create(self, project_id, skill_id):
        """Link a skill to a project."""
        self._run("INSERT INTO ProjectSkills (project_id, skill_id) VALUES (?, ?)", (project_id, skill_id))

    def getById(self, project_id, skill_id):
        """Retrieve a specific project-skill link."""
        rows = self._run(
            "SELECT * FROM ProjectSkills WHERE project_id = ? AND skill_id = ?",
            (project_id, skill_id),
            fetch=True
        )
        return rows[0] if rows else None

    def delete(self, project_id, skill_id):
        """Remove a skill from a project."""
        self._run("DELETE FROM ProjectSkills WHERE project_id = ? AND skill_id = ?", (project_id, skill_id))

    def listAll(self):
        """List all project-skill relationships."""
        return self._run("SELECT * FROM ProjectSkills", fetch=True)
