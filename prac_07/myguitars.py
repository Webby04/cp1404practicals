from guitar import Guitar

FILENAME = "guitars.csv"

def main():
    """Read guitars from file and display them."""
    guitars = []
    with open(FILENAME, 'r') as csvfile:
        for line in csvfile:
            name, year, cost = line.strip().split(',')
            guitar = Guitar(name, int(year), float(cost))
            guitars.append(guitar)

    for guitar in guitars:
        print(guitar)


main()