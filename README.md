# Co-Cre8

# Co-Cre8 – Project Partners On-Demand

Co-Cre8 is a console-based Python + SQLite application that allows users to create, showcase, and join collaborative projects. It's built to help people find project partners and contribute to real-world ideas.

---

## Features

- Users can register and manage their profiles.
- Projects can be created, browsed, and filtered by skill.
- Skills are tagged to projects.
- Users can join and contribute to any project.
- Internal messaging system for communication.
- Search, sort, and recursion examples included.

---

```
projectmatch/
├── db_schema.py           # Creates and initializes all tables
├── main.py                # App entry point and console menu
├── functions.py           # 10+ utility functions (recursion, sort, search)
├── models/
│   ├── base_model.py      # Shared DB logic
│   ├── user.py            # User table methods
│   ├── project.py         # Project table methods
│   ├── membership.py      # Project membership
│   ├── skill.py           # Skill management
│   ├── projectSkill.py    # Links skills to projects
│   └── message.py         # Project messaging
└── README.md              # Instructions and reflection
```

### How to Run Co-Cre8
Requirements
Python 3.7 or higher

No external libraries needed (uses Python’s built-in sqlite3)

######### Setup & Execution
Clone or download the project folder:

git clone https://github.com/josedata6/CoCre8.git
cd co-cre8
Run the application:

python main.py
This will automatically create the database (projectmatch.db) if it doesn’t exist.

You’ll see an interactive menu in your terminal to create projects, join them, search, and more.
