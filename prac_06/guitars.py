"""
Guitar
Estimate: 25 minutes
Actual:   23 minutes
"""

from prac_06.guitar import Guitar

def main():
    """Guitar program"""
    guitars = []

    print("My guitars!")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        add_guitar = Guitar(name, year, cost)
        guitars.append(add_guitar)
        print(f"{add_guitar} added.")
        name = input("Name: ")


    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

main()