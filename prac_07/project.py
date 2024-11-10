"""
Project
Estimate: 90 minutes
Actual:   23 minutes
"""

class Project:
    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        self.name = name
        self.start_date = start_date
        self.priority = int(priority)
        self.cost_estimate = float(cost_estimate)
        self.completion_percentage = int(completion_percentage)

    def __str__(self):
        return (f"{self.name}, start: {self.start_date}, priority {self.priority}, estimate: $"
                f"{self.cost_estimate:,.2f}, completion: {self.completion_percentage}%")

    def __lt__(self, other):
        """Compare projects by priority (ascending)."""
        return self.priority < other.priority

    def __gt__(self, other):
        """Compare two projects by start date (ascending)"""
        return self.start_date > other.start_date

    def is_complete(self):
        """Return True if projects is 100% complete."""
        return self.completion_percentage == 100

    def update_percentage(self, new_percentage):
        self.completion_percentage = new_percentage

    def update_priority(self, new_priority):
        self.priority = new_priority

