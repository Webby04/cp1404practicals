class Band:
    """Band class for storing details of a band and its musicians."""

    def __init__(self, name=""):
        """Initialise a Band with a name and an empty list of musicians."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string representation of a Band and its musicians."""
        musician_info = ', '.join([f"{musician.name} ({musician.instruments})" for musician in self.musicians])
        return f"{self.name} ({musician_info})"

    def __repr__(self):
        """Return a string representation of a Band with its details."""
        return str(self)

    def add(self, musician):
        """Add a Musician to the Band."""
        self.musicians.append(musician)

    def play(self):
        """Return a string showing each musician playing their first instrument, or no instrument."""
        return '\n'.join([musician.play() for musician in self.musicians])
