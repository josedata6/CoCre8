from models.project import Project
from models.user import User
from models.skill import Skill
from models.projectSkill import ProjectSkill
from models.membership import Membership
from models.message import Message

# Recursive: Walks a hypothetical linked project chain
def findProjectChain(project_id, depth=0, visited=None):
    """Recursive mock to simulate a dependency walk (e.g., linked project threads)."""
    if visited is None:
        visited = set()
    if project_id in visited or depth > 10:
        return []
    visited.add(project_id)
    return [project_id] + findProjectChain(project_id + 1, depth + 1, visited)

def listUsersByKeyword(keyword):
    """Return users whose name or bio contains the keyword."""
    return [u for u in User().listAll() if keyword.lower() in (u[1]+u[3]).lower()]

def listProjectsBySkill(skill_name):
    """Return projects that are tagged with a given skill."""
    skill_id = None
    for s in Skill().listAll():
        if s[1].lower() == skill_name.lower():
            skill_id = s[0]
            break
    if not skill_id:
        return []
    pskill = [ps[0] for ps in ProjectSkill().listAll() if ps[1] == skill_id]
    return [p for p in Project().listAll() if p[0] in pskill]

def binarySearch(sorted_list, target):
    """Classic binary search (recursive)."""
    if not sorted_list:
        return -1
    mid = len(sorted_list) // 2
    if sorted_list[mid] == target:
        return mid
    if target < sorted_list[mid]:
        return binarySearch(sorted_list[:mid], target)
    result = binarySearch(sorted_list[mid + 1:], target)
    return mid + 1 + result if result != -1 else -1

def quickSort(arr):
    """Simple quick sort (recursive)."""
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    lesser = quickSort([x for x in arr[1:] if x < pivot])
    greater = quickSort([x for x in arr[1:] if x >= pivot])
    return lesser + [pivot] + greater

def getAllProjectTitlesSorted():
    """Returns project titles sorted alphabetically using quickSort."""
    titles = [p[1] for p in Project().listAll()]
    return quickSort(titles)

def getMessagesForProject(project_id):
    """Returns all messages sent to a specific project."""
    return [m for m in Message().listAll() if m[2] == project_id]

def countProjectsPerUser():
    """Returns a dictionary of user_id to number of projects created."""
    count = {}
    for project in Project().listAll():
        uid = project[3]
        count[uid] = count.get(uid, 0) + 1
    return count

def getTopContributors():
    """Returns user(s) who joined the most projects."""
    count = {}
    for m in Membership().listAll():
        uid = m[0]
        count[uid] = count.get(uid, 0) + 1
    max_contrib = max(count.values(), default=0)
    return [uid for uid, c in count.items() if c == max_contrib]

def findProjectByTitle(keyword):
    """Returns list of projects matching keyword in title."""
    return [p for p in Project().listAll() if keyword.lower() in p[1].lower()]
