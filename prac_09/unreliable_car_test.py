from prac_09.unreliable_car import UnreliableCar

def main():
    """Testing UnreliableCars."""
    good_car = UnreliableCar("Good", 50, 100)
    faulty_car = UnreliableCar("Faulty", 75, 30)

    for i in range(1, 10):
        print(f"Attempting to drive {i}km:")
        print(f"{good_car.name:12} drove {good_car.drive(i):2}km")
        print(f"{faulty_car.name:12} drove {faulty_car.drive(i):2}km")

    print(good_car)
    print(faulty_car)

main()