from db_schema import initDb
from functions import (
    listUsersByKeyword, listProjectsBySkill, getAllProjectTitlesSorted,
    getMessagesForProject, countProjectsPerUser, getTopContributors,
    findProjectByTitle, findProjectChain
)
from models.user import User
from models.project import Project
from models.membership import Membership
from models.message import Message
import datetime

def menu():
    print("\n--- ProjectMatch Main Menu ---")
    print("1. List users by keyword")
    print("2. List projects by skill")
    print("3. Show sorted project titles")
    print("4. Show messages for a project")
    print("5. Show project counts per user")
    print("6. Show top project contributors")
    print("7. Search projects by title")
    print("8. Demo recursive project chain")
    print("9. Exit")

def main():
    initDb()
    print("Welcome to ProjectMatch!")
    while True:
        menu()
        choice = input("Choose an option: ").strip()
        if choice == "1":
            kw = input("Enter a keyword: ")
            for u in listUsersByKeyword(kw):
                print(u)
        elif choice == "2":
            sk = input("Enter skill name: ")
            for p in listProjectsBySkill(sk):
                print(p)
        elif choice == "3":
            print(getAllProjectTitlesSorted())
        elif choice == "4":
            pid = int(input("Enter project ID: "))
            for m in getMessagesForProject(pid):
                print(m)
        elif choice == "5":
            print(countProjectsPerUser())
        elif choice == "6":
            print("Top contributors (user_id):", getTopContributors())
        elif choice == "7":
            kw = input("Enter title keyword: ")
            for p in findProjectByTitle(kw):
                print(p)
        elif choice == "8":
            pid = int(input("Enter start project ID: "))
            print("Project chain:", findProjectChain(pid))
        elif cho
