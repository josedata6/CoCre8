from models.base_model import BaseModel

class User(BaseModel):
    def create(self, name, email, bio):
        """Add a new user to the database."""
        self._run("INSERT INTO Users (name, email, bio) VALUES (?, ?, ?)", (name, email, bio))

    def getById(self, user_id):
        """Retrieve a user by ID."""
        rows = self._run("SELECT * FROM Users WHERE user_id = ?", (user_id,), fetch=True)
        return rows[0] if rows else None
#This line defines a method called update that takes a user_id and optional parameters name, email, and bio.
    def update(self, user_id, name=None, email=None, bio=None): 
        """Update fields of a user by ID."""
        fields, values = [], [] #This line creates two empty lists called fields and values.
        if name:
            fields.append("name = ?") #This line adds the string "name = ?" to the fields list.
            values.append(name)
        if email:
            fields.append("email = ?")
            values.append(email)
        if bio:
            fields.append("bio = ?")
            values.append(bio)
        values.append(user_id)
        #This line constructs an SQL query string that updates the Users table.
        sql = f"UPDATE Users SET {', '.join(fields)} WHERE user_id = ?"
        self._run(sql, tuple(values))

    def delete(self, user_id):
        """Remove a user from the database."""
        self._run("DELETE FROM Users WHERE user_id = ?", (user_id,))

    def listAll(self):
        """List all users."""
        return self._run("SELECT * FROM Users", fetch=True)
