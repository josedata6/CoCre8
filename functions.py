# Import model classes that interface with each database table
from models.project import Project            # For accessing project records
from models.user import User                  # For accessing user records
from models.skill import Skill                # For accessing skill records
from models.projectSkill import ProjectSkill  # For linking projects to skills
from models.membership import Membership      # For managing project memberships
from models.message import Message            # For accessing project messages

# Recursive function: simulate a walk through a hypothetical chain of linked projects
def findProjectChain(project_id, depth=0, visited=None):
    """
    Stops if a project has been visited already or recursion exceeds 10 levels.
    Returns a list of project IDs in the chain."""
    if visited is None:
        visited = set()
    if project_id in visited or depth > 10: #base case
        return []
    visited.add(project_id)
    return [project_id] + findProjectChain(project_id + 1, depth + 1, visited)

# Filter users whose name or bio contains a keyword
def listUsersByKeyword(keyword):
    """Return users whose name or bio contains the keyword (case-insensitive)."""
    return [u for u in User().listAll() if keyword.lower() in (u[1] + u[3]).lower()]

# Filter projects by a matching skill
def listProjectsBySkill(skill_name):
    """
    Return a list of projects that require a specific skill.
    Searches Skills table, finds matching skill ID, and links it to projects.
    """
    skill_id = None
    for s in Skill().listAll():
        if s[1].lower() == skill_name.lower():
            skill_id = s[0]
            break
    if not skill_id:
        return []
    # Get all project IDs that include this skill
    # Go through all the project-skill pairs, and collect the project IDs where the skill ID matches the one we're looking for.
    pskill = [ps[0] for ps in ProjectSkill().listAll() if ps[1] == skill_id]
    return [p for p in Project().listAll() if p[0] in pskill]

# Binary search: classic recursive version
def binarySearch(sorted_list, target):
    """Recursively search for a value in a sorted list. Returns index or -1 if not found."""
    if not sorted_list:
        return -1
    mid = len(sorted_list) // 2
    if sorted_list[mid] == target:
        return mid
    if target < sorted_list[mid]:
        return binarySearch(sorted_list[:mid], target)
    result = binarySearch(sorted_list[mid + 1:], target)
    return mid + 1 + result if result != -1 else -1

# Recursive quick sort algorithm
def quickSort(arr):
    """Recursively sorts a list using quick sort algorithm."""
    if len(arr) <= 1:
        return arr
    pivot = arr[0] # Choose the first element as pivot
    lesser = quickSort([x for x in arr[1:] if x < pivot]) # elements less than pivot
    greater = quickSort([x for x in arr[1:] if x >= pivot]) # elements greater than or equal to pivot
    return lesser + [pivot] + greater

# Get sorted project titles alphabetically
def getAllProjectTitlesSorted():
    """Return a list of all project titles sorted alphabetically."""
    titles = [p[1] for p in Project().listAll()]  # Extract only titles (index 1)
    return quickSort(titles)

# Return all messages tied to a given project ID
def getMessagesForProject(project_id):
    """Returns all messages posted to a specific project."""
    return [m for m in Message().listAll() if m[2] == project_id]

# Count how many projects each user has created
def countProjectsPerUser():
    """Returns a dictionary of user_id to number of projects they’ve created."""
    count = {}
    for project in Project().listAll():
        uid = project[3]  # created_by field
        count[uid] = count.get(uid, 0) + 1
    return count

# Identify the user(s) who joined the most projects
def getTopContributors():
    """Returns a list of user_ids for those who joined the most projects."""
    count = {}
    for m in Membership().listAll():
        uid = m[0]  # user_id
        count[uid] = count.get(uid, 0) + 1
    max_contrib = max(count.values(), default=0)
    return [uid for uid, c in count.items() if c == max_contrib] # list of user_ids with max contributions

# Search for projects with a matching keyword in the title
def findProjectByTitle(keyword):
    """Returns a list of projects where the title contains the given keyword."""
    return [p for p in Project().listAll() if keyword.lower() in p[1].lower()]
