from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"

def main():
    """Main menu for taxi simulation."""
    total_bill = 0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    print("Let's drive!")
    print(MENU)
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "c":
            print("Taxis available:")
            display_taxis(taxis)
            current_taxi = select_taxi(current_taxi, taxis)
        elif choice == "d":
            total_bill = drive_taxi(current_taxi, total_bill)
        else:
            print("Invalid option")
        print(f"Bill to date: ${total_bill:.2f}")
        print(MENU)
        choice = input(">>> ").lower()
    print(f"Total trip cost: ${total_bill:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)


def display_taxis(taxis):
    """Display the list of available taxis"""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")

def select_taxi(current_taxi, taxis):
    """Let the user choose a taxi and return it."""
    choose_taxi = int(input("Choose taxi: "))
    try:
        current_taxi = taxis[choose_taxi]
    except IndexError:
        print("Invalid taxi choice")
    return current_taxi

def drive_taxi(current_taxi, total_bill):
    """Get the driving distance, calculate the fare, and update the total bill."""
    if current_taxi:
        current_taxi.start_fare()
        driving_distance = float(input("Drive how far? "))
        current_taxi.drive(driving_distance)
        cost_of_trip = current_taxi.get_fare()
        print(f"Your {current_taxi.name} trip cost you ${cost_of_trip:.2f}")
        total_bill += cost_of_trip
    else:
        print("You need to choose a taxi before you can drive")
    return total_bill


main()