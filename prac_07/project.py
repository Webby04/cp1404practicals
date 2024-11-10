"""
Project
Estimate: 90 minutes
Actual:   23 minutes
"""
import datetime

class Project:
    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        self.name = name
        self.start_date = start_date
        self.priority = int(priority)
        self.cost_estimate = float(cost_estimate)
        self.completion_percentage = int(completion_percentage)

    def __str__(self):
        return (f"{self.name}, start: {self.start_date}, priority {self.priority}, estimate: $"
                f"{self.cost_estimate}, completion: {self.completion_percentage}%")

    def is_complete(self):
        """Return True if projects is 100% complete."""
        return self.completion_percentage == 100
