"""
Guitar
Estimate: 20 minutes
Actual:   18 minutes
"""

CURRENT_YEAR = 2022
VINTAGE_AGE = 50


class Guitar:
    """Represent a guitar object."""

    def __init__(self, name="", year=0, cost=0):
        """Initialise a Guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return the name, year and cost values."""
        return f"{self.name} ({self.year}) : ${self.cost:.2f}"

    def get_age(self):
        """Returns the age guitar"""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Returns True if the item is considered vintage based on its age."""
        return self.get_age() >= VINTAGE_AGE

    def __lt__(self, other):
        """Compare Guitars by year for sorting"""
        return self.year < other.year