"""
Guitar
Estimate: 20 minutes
Actual:   23 minutes
"""

from prac_06.guitar import Guitar

def main():
    """Tests for Guitar class."""
    name = "Gibson L-5 CES"
    year = 1922
    cost = 16035.40

    guitar = Guitar(name, year, cost)
    other_guitar = Guitar("Another Guitar", 2013, cost)

    print(f"{guitar.name} get_age() - Expected 100. Got {guitar.get_age()}")
    print(f"{other_guitar.name} get_age() - Expected 9. Got {other_guitar.get_age()}")
    print(f"{guitar.name} get_vintage() - Expected True. Got {guitar.is_vintage()}")
    print(f"{other_guitar.name} get_vintage() - Expected False. Got {other_guitar.is_vintage()}")

main()
