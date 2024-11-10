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
            projects = load_projects_from_file()
        elif choice == "S":
            save_projects_to_file(projects)
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            filter_projects(projects)
        elif choice == "A":
            add_project(projects)
        elif choice == "U":
            update_project(projects)
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").upper()
    save_projects(projects)


def load_projects(filename):
    """Load projects from CSV file and return list of Project objects."""
    projects = []
    with open(filename, 'r') as file:
        file.readline()  # Skip header
        for line in file:
            # Split by commas and unpack the 5 values
            name, start_date, priority, cost_estimate, completion_percentage = line.strip().split('\t')
            # Create a Project object with the converted start_date
            project = Project(name, start_date, int(priority), float(cost_estimate), int(completion_percentage))
            projects.append(project)
    return projects


def load_projects_from_file():
    """Load projects from specific CSV file and return list of Project objects."""
    load_filename = input("Filename: ")
    projects = load_projects(load_filename)
    print(f"Loaded {len(projects)} projects from {load_filename}")
    return projects

def save_projects(projects):
    """Save the current projects to file."""
    save_results = input(f"Would you like to save to {FILENAME}? ").lower()
    if save_results != "no":
        with open(FILENAME, "w") as file:
            for project in projects:
                file.write(f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t{project.priority}\t"
                           f"{project.cost_estimate}\t{project.completion_percentage}\n")
        print(f"Projects saved to {FILENAME}")
    print("Thank you for using custom-built project management software.")

def save_projects_to_file(projects):
    """Save the current projects to a specified file."""
    save_filename = input("Enter filename to save to: ")
    with open(save_filename, "w") as file:
        for project in projects:
            file.write(f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t{project.priority}\t"
                       f"{project.cost_estimate}\t{project.completion_percentage}\n")
    print(f"Projects saved to {save_filename}")


def display_projects(projects):
    """Display projects by complete and incomplete projects."""
    incomplete_projects = [project for project in projects if not project.is_complete()]
    complete_projects = [project for project in projects if project.is_complete()]
    print("Incomplete projects:")
    for project in sorted(incomplete_projects):
        print(f"  {project}")
    print("Completed projects:")
    for project in sorted(complete_projects):
        print(f"  {project}")


def filter_projects(projects):
    """Filter projects that start after specific date"""
    is_valid_input = False
    while not is_valid_input:
        date_string = input("Show projects that start after date (dd/mm/yyyy): ")
        try:
            date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
            filtered_projects = [project for project in projects if project.start_date.date() >= date]

            if filtered_projects:
                filtered_projects.sort()
                for project in filtered_projects:
                    print(project)
            else:
                print(f"No projects start after {date.strftime('%d/%m/%Y')}.")
            is_valid_input = True
        except ValueError:
            print("Invalid date format. Please enter the date in dd/mm/yyyy format.")


def add_project(projects):
    """Add a new project to the list of projects."""
    print("Let's add a new project")
    add_name = input("Name: ").title()
    while add_name == "":
        print("Name cannot be blank")
        add_name = input("Name: ").title()
    add_date = 0
    is_valid_input = False
    while not is_valid_input:
        add_date = input("Start date (dd/mm/yyyy): ")
        try:
            datetime.datetime.strptime(add_date, "%d/%m/%Y").date()
            is_valid_input = True
        except ValueError:
            print("Invalid date format. Please enter the date in dd/mm/yyyy format.")
    add_priority = 0
    is_valid_input = False
    while not is_valid_input:  # Make sure priority input is valid
        try:
            add_priority = int(input("Priority: "))
            if add_priority == "":
                print("Input can not be blank")
            elif add_priority > 0:
                is_valid_input = True
            else:
                print("Number must be > 0")
        except ValueError:
            print("Invalid input; enter a valid number")
    add_cost = 0
    is_valid_input = False
    while not is_valid_input:  # Make sure priority input is valid
        try:
            add_cost = float(input("Cost estimate: $"))
            if add_cost == "":
                print("Cost estimate cannot be blank")
            elif add_cost >= 0:
                is_valid_input = True
            else:
                print("Cost estimate must be >= 0")
        except ValueError:
            print("Invalid input; enter a valid number")
    add_percentage = 0
    is_valid_input = False
    while not is_valid_input:
        try:
            add_percentage = int(input("Percent complete: "))
            if add_percentage == "":
                print("Percent estimate cannot be blank")
            elif 0 <= add_percentage <= 100:
                is_valid_input = True
            else:
                print("Percent estimate must be >= 0 and <= 100")
        except ValueError:
            print("Invalid input; enter a valid number")
    project = Project(add_name, add_date, int(add_priority), float(add_cost), int(add_percentage))
    projects.append(project)

def update_project(projects):
    """Select a project and update its completion percentage and priority"""
    for index, project in enumerate(projects, 0):
        print(f"{index} {project}")
    project_choice = 0
    is_valid_input = False
    while not is_valid_input:
        project_choice = input("Project choice: ")
        if project_choice == "":
            print("Project choice cannot be blank")
        else:
            try:
                project_choice = int(project_choice)
                if 0 <= project_choice <= (len(projects) - 1):
                    is_valid_input = True
                else:
                    print("Invalid place number")
            except ValueError:
                print("Invalid input; enter a valid number")
    for index, project in enumerate(projects, 0):
        if index == project_choice:
            print(project)
            try:
                new_percentage = input("New percentage: ")
                if new_percentage != "":
                    while not (0 <= int(new_percentage) <= 100):
                        print("Invalid percentage; it must be between 0 and 100")
                        new_percentage = input("New percentage: ")
                    project.update_percentage(int(new_percentage))
            except ValueError:
                print("Invalid input; enter a valid number")
            try:
                new_priority = input("New priority: ")
                if new_priority != "":
                    while not (0 <= int(new_priority) <= len(projects)):
                        print(f"Invalid priority; it must be between 0 and {len(projects)}")
                        new_priority = input("New priority: ")
                    project.update_priority(int(new_priority))
            except ValueError:
                print("Invalid input; enter a valid number")




main()
