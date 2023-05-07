import datetime


class Project:
    """Represent information about a project."""

    def __init__(self, name, start_date, priority=0, cost_estimate=0.0, completion_percentage=0):
        """Construct a Project from the given values."""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        """Return string representation of a Project."""
        return f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, priority {self.priority}, estimate: ${self.cost_estimate}, completion: {self.completion_percentage}% "

    def __repr__(self):
        """Return string representation of a Project."""
        return f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, priority {self.priority}, estimate: ${self.cost_estimate}, completion: {self.completion_percentage}% "

    def __lt__(self, other):
        """Sort the list of projects based on priority number."""
        return self.priority < other.priority
