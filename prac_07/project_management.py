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
    print("Welcome to Pythonic Project Management")
    projects = load_projects()
    print(f"Loaded {len(projects)} from {FILENAME}")
    print(MENU)
    choice = input(">>> ").upper()



def load_projects():
    """Load projects from CSV file and return list of Project objects."""
    projects = []
    with open(FILENAME, 'r') as file:
        file.readline() # Skip header
        for line in file:
            # Split by commas and unpack the 5 values
            name, start_date, priority, cost_estimate, completion_percentage = line.strip().split('\t')
            # Create a Project object with the converted start_date
            project = Project(name, start_date, int(priority), float(cost_estimate), int(completion_percentage))
            projects.append(project)
    return projects



main()