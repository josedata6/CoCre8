# Import database initializer
from db_schema import initDb

# Import model classes to interact with database tables
from models.user import User
from models.project import Project
from models.membership import Membership
from models.message import Message

# imports specific functions from functions.py 
# file so you can use them in script
# without importing everything from the file.
from functions import (
    listUsersByKeyword, listProjectsBySkill, getAllProjectTitlesSorted,
    getMessagesForProject, countProjectsPerUser, getTopContributors,
    findProjectByTitle
)

import datetime  # For generating join date

# Display the menu options for the user
def menu():
    print("\n--- Co-Cre8 Main Menu ---")
    print("1. List users by keyword")
    print("2. List projects by skill")
    print("3. Show sorted project titles")
    print("4. Show messages for a project")
    print("5. Show project counts per user")
    print("6. Show top project contributors")
    print("7. Search projects by title")
    print("8. Create a new project")
    print("9. Join an existing project")
    print("0. Exit")

# Main function: runs the application
def main():
    initDb()  # Initialize database and tables (if not already created)
    print("Welcome to Co-Cre8!")

    # Application loop: keeps running until the user chooses to exit
    while True:
        menu()
        choice = input("Choose an option: ").strip() # Get user input for menu choice

        # 1. List users whose name or bio matches a keyword
        if choice == "1":
            kw = input("Enter a keyword: ")
            for u in listUsersByKeyword(kw): # List users that match the keyword
                print(u)

        # 2. List projects that are tagged with a specific skill
        elif choice == "2": # List projects by skill
            sk = input("Enter skill name: ") # Get skill name from user
            for p in listProjectsBySkill(sk): # List projects that match the skill
                print(p)

        # 3. Display all project titles sorted alphabetically
        elif choice == "3": # Show sorted project titles
            print(getAllProjectTitlesSorted())

        # 4. Show all messages posted in a specific project
        elif choice == "4":
            pid = int(input("Enter project ID: "))
            for m in getMessagesForProject(pid): # Get messages for the project
                print(m) # Print each message

        # 5. Count and display how many projects each user has created
        elif choice == "5":
            print(countProjectsPerUser()) # Count projects per user

        # 6. Identify and show user(s) who joined the most projects
        elif choice == "6": # Show top contributors
            print("Top contributors (user_id):", getTopContributors())

        # 7. Search for projects with a keyword in their title
        elif choice == "7":
            kw = input("Enter title keyword: ")
            for p in findProjectByTitle(kw): # Find projects by title
                print(p)

        # 8. Create a new project and assign the current user as creator
        elif choice == "8":
            user_id = int(input("Enter your user ID: ")) # Get user ID
            title = input("Enter project title: ")
            desc = input("Enter description: ")
            Project().create(title, desc, user_id) # Create a new project
            print("Project created.")

        # 9. Join a project with a specific role and today's date
        elif choice == "9":
            user_id = int(input("Enter your user ID: "))
            pid = int(input("Enter the project ID you want to join: "))
            role = input("Enter your role (e.g., developer, designer): ")
            today = datetime.date.today().isoformat() # Format date as YYYY-MM-DD
            Membership().create(user_id, pid, role, today)
            print("Successfully joined the project.")

        # 0. Exit the application
        elif choice == "0":
            print("Goodbye from Co-Cre8!")
            break

        # Handle invalid input
        else:
            print("Invalid option.")

# Run the main function if the script is executed directly
if __name__ == "__main__":
    main()
