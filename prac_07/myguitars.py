from guitar import Guitar

FILENAME = "guitars.csv"

def main():
    """Read guitars from file and display them."""
    guitars = load_guitars()
    guitars.sort()
    display_guitars(guitars)


def load_guitars():
    """Load guitars from CSV file and return list of Guitar objects."""
    guitars = []
    with open(FILENAME, 'r') as csvfile:
        for line in csvfile:
            name, year, cost = line.strip().split(',')
            guitar = Guitar(name, int(year), float(cost))
            guitars.append(guitar)
    return guitars


def display_guitars(guitars):
    """Display all the guitars in the list."""
    for guitar in guitars:
        print(guitar)


main()