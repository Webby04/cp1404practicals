"""
Programming Language
Estimate: 22 minutes
Actual:   25 minutes
"""


class ProgrammingLanguage:
    """Represent a programming language object."""

    def __init__(self, name, typing, reflection, year):
        """Initialise a programming language instance."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Return the details for different languages."""
        return f"{self.name}, {self.typing}, Reflection={self.is_dynamic()}, First appeared in {self.year}"

    def is_dynamic(self):
        """Determine if language is dynamic."""
        return self.typing == 'Dynamic'
