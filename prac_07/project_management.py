"""
Project Management
Estimate: 90 minutes
Actual:   23 minutes
"""

from project import Project
import datetime

FILENAME = "projects.txt"

MENU = ("- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects "
        "by date\n- (A)dd new project\n- (U)pdate project\n- (Q)uit")

def main():
    """Menu for project management."""
    print("Welcome to Pythonic Project Management")
    projects = load_projects(FILENAME)
    print(f"Loaded {len(projects)} from {FILENAME}")
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            load_projects_from_file()



def load_projects(filename):
    """Load projects from CSV file and return list of Project objects."""
    projects = []
    with open(filename, 'r') as file:
        file.readline() # Skip header
        for line in file:
            # Split by commas and unpack the 5 values
            name, start_date, priority, cost_estimate, completion_percentage = line.strip().split('\t')
            # Create a Project object with the converted start_date
            project = Project(name, start_date, int(priority), float(cost_estimate), int(completion_percentage))
            projects.append(project)
    return projects

def load_projects_from_file():
    """Load projects from specific CSV file and return list of Project objects."""
    filename = input("Filename: ")
    projects = load_projects(filename)
    print(f"Loaded {len(projects)} projects from {filename}")
    return projects



main()