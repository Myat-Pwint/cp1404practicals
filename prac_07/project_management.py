import datetime
from prac_07.project import project


MENU = "(L)"
FILENAME = "projects.txt"
projects = []


def load_projects(self):
    """
    Load projects from a file.
    """
    filename = input("Enter filename: ")
    with open(filename) as f:
        next(f)  # skip header
        for line in f:
            name, start_date, priority, cost_estimate, completion_percentage = line.strip().split("\t")
            start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
            priority = int(priority)
            cost_estimate = float(cost_estimate)
            completion_percentage = int(completion_percentage)
            project = Project(name, start_date, priority, cost_estimate, completion_percentage)
            self.projects.append(project)
    print(f"{len(self.projects)} projects loaded from {filename}")

def save_projects(self):
    """
    Save projects to a file.
    """
    filename = input("Enter filename: ")
    with open(filename, "w") as f:
        print("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage", file=f)
        for project in self.projects:
            print(f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t{project.priority}\t{project.cost_estimate:.2f}\t{project.completion_percentage}", file=f)
    print(f"{len(self.projects)} projects saved to {filename}")

def display_projects(self):
    """
    Display all projects, grouped by complete/incomplete and sorted by priority.
    """
    incomplete = []
    complete = []
    for project in self.projects:
        if project.completion_percentage == 100:
            complete.append(project)
        else:
            incomplete.append(project)
    incomplete = sorted(incomplete, key=lambda x: x.priority)
    complete = sorted(complete, key=lambda x: x.priority)
    print("Incomplete projects:")
    for project in incomplete:
        print(f"  {project}")
    print("Completed projects:")
    for project in complete:
        print(f"  {project}")

def filter_projects_by_date(self):
    """
    Filter projects by start date.
    """
    date_string = input("Enter date (d/m/yyyy): ")
    date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
    filtered_projects = [project for project in self.projects if project.start_date > date]
    filtered_projects = sorted(filtered_projects, key=lambda x: x.start_date)
    for project in filtered_projects:
        print(project)

def add_project(self):
    """
    Add a new project.
    """
    print("Let's add a new project")
    name = input("Name: ")
    start_date_string = input("Start date (dd/mm/yyyy): ")
    start_date = datetime.datetime.strptime(start_date_string, "%d/%m/%Y").date()
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: $"))
    completion_percentage =