from kivy.app import App
from kivy.lang import Builder

from kivy.properties import StringProperty

MILES_TO_KM = 1.60934


class MilesToKilometersApp(App):
    """A Kivy App to convert miles to kilometers."""
    output_km = StringProperty()

    def build(self):
        """Build the Kivy app from the kv file """
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self):
        """Convert miles to kilometers and update the output label."""

        value = self.get_validated_miles()
        result = value * MILES_TO_KM
        self.output_km = str(result)
        self.root.ids.output_label.text = self.output_km

    def handle_increment(self, change):
        """Increment or decrement the miles input value."""
        value = self.get_validated_miles() + change
        self.root.ids.input_miles.text = str(value)
        self.handle_calculate()

    def get_validated_miles(self):
        """Validate and return the miles input as a float, or 0 if invalid."""
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0


MilesToKilometersApp().run()
