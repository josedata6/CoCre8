# ProjectMatch

# ProjectMatch – Project Partners On-Demand

ProjectMatch is a console-based Python + SQLite application that allows users to create, showcase, and join collaborative projects. It's built to help people find project partners and contribute to real-world ideas.

---

## Features

- Users can register and manage their profiles.
- Projects can be created, browsed, and filtered by skill.
- Skills are tagged to projects.
- Users can join and contribute to any project.
- Internal messaging system for communication.
- Search, sort, and recursion examples included.

---

####
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


 --->
