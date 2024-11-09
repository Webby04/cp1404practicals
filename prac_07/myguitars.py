from guitar import Guitar

FILENAME = "guitars.csv"

def main():
    """Read guitars from file and display them."""
    guitars = load_guitars()
    add_guitars(guitars)
    guitars.sort()
    display_guitars(guitars)
    save_guitar(guitars)


def load_guitars():
    """Load guitars from CSV file and return list of Guitar objects."""
    guitars = []
    with open(FILENAME, 'r') as csvfile:
        for line in csvfile:
            name, year, cost = line.strip().split(',')
            guitar = Guitar(name, int(year), float(cost))
            guitars.append(guitar)
    return guitars

def add_guitars(guitars):
    """Add new guitars to guitars list."""
    name = input("Name: ")
    year = int(input("Year: "))
    cost = float(input("Cost: $"))
    add_guitar = Guitar(name, year, cost)
    guitars.append(add_guitar)

def display_guitars(guitars):
    """Display all the guitars in the list."""
    for guitar in guitars:
        print(guitar)

def save_guitar(guitars):
    """Write the list of guitars to the CSV file."""
    with open(FILENAME, "w") as csvfile:
        for guitar in guitars:
            csvfile.write(f"{guitar.name},{guitar.year},{guitar.cost:.2f}\n")

main()