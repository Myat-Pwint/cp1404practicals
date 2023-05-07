import datetime
from prac_07.project import Project
from operator import itemgetter

MENU = "(L)oad projects\n(S)ave projects\n(D)isplay projects\n(F)ilter projects by date\n(A)dd new project\n(U)pdate " \
       "project\n(Q)uit"
FILENAME = "projects.txt"
projects = []


def main():
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            load_projects(FILENAME)
        elif choice == "S":
            save_projects(FILENAME)
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            filter_projects_by_date()
        elif choice == "A":
            add_projects()
        elif choice == "U":
            update_projects()
        else:
            print("Invalid input")

        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you for using custom-built project management software.")


def load_projects(FILENAME):
    """Load projects from a file."""
    with open(FILENAME, "r") as file:
        file.readline()
        for line in file:
            name, start_date, priority, cost_estimate, completion_percentage = line.strip().split("\t")
            start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
            projects.append(Project(name, start_date, int(priority), float(cost_estimate), int(completion_percentage)))
    return projects


def save_projects(FILENAME):
    """Save updated projects to projects.txt"""
    with open(FILENAME, "w") as out_file:
        out_file.write("Name\tStart Date\tPriority\tEstimate\tCompletion Percentage\n")
        for project in projects:
            out_file.write(
                f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t{project.priority}\t{project.cost_estimate:.2f}\t{project.completion_percentage}\n")


def display_projects(projects):
    """Display all projects, grouped by complete/incomplete and sorted by priority."""
    store_projects = [
        {"project": project, "priority": project.priority, "completion_percentage": project.completion_percentage}
        for project in projects]
    incomplete_projects = sorted([item for item in store_projects if item["completion_percentage"] < 100],
                                 key=itemgetter("priority"))
    completed_projects = sorted([item for item in store_projects if item["completion_percentage"] == 100],
                                key=itemgetter("priority"))

    print("Incomplete projects: ")
    for item in incomplete_projects:
        print(f"    {item['project']}")
    print("Complete projects: ")
    for item in completed_projects:
        print(f"    {item['project']}")


def filter_projects_by_date():
    """Filter projects by start date."""
    filtered_date = input("Show projects that start after date (dd/mm/yy): ")
    filtered_date = datetime.datetime.strptime(filtered_date, "%d/%m/%Y").date()
    filtered_projects = []
    filtered_projects = [project for project in projects if project.start_date > filtered_date]
    filtered_projects.sort()
    for filtered_project in filtered_projects:
        print(filtered_project)


def add_projects():
    """Add a new project."""
    print(f"Let's add a new project")
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yyyy): ")
    start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: $"))
    completion_percentage = int(input("Percent complete: "))
    new_project = Project(name, start_date, priority, cost_estimate, completion_percentage)
    projects.append(new_project)


def update_projects():
    """Update projects """
    for number, project in enumerate(projects, 0):
        print(f"{number}, {project}")
    project_choice = int(input("Project choice: "))
    selected_project = projects[project_choice]
    print(selected_project)
    new_completion = input("New Percentage: ")
    new_priority = input("New Priority: ")
    if new_completion:
        selected_project.completion_percentage = int(new_completion)
    if new_priority:
        selected_project.priority = int(new_priority)


main()