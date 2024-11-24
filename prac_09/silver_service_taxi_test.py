"""
CP1404/CP5632 Practical - Suggested Solution
SilverServiceTaxi class tests
"""

from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    """Test SilverServiceTaxi."""
    taxi = SilverServiceTaxi("Hummer", 200, 2)
    taxi.drive(10)
    print(taxi)
    print(taxi.get_fare())

main()