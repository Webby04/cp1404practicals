from prac_09.taxi import Taxi

class SilverServiceTaxi(Taxi):
    """Represents a SilverServiceTaxi."""

    flagfall = 4.5

    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi instance with fanciness and flagfall."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def __str__(self):
        """Return a string representation of the taxi, including the flagfall."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"


    def get_fare(self):
        """Get current fare"""
        return super().get_fare() + self.flagfall

