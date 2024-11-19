from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    """Kivy app to demo dynamic label creation. """

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        self.names = {'Lachlan', 'Bob', 'Fred', 'Jeff', 'Oren'}

    def build(self, **kwargs):
        """Build the Kivy GUI."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels1.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        for name in self.names:
            label = Label(text=name, font_size=32)
            self.root.ids.main.add_widget(label)




DynamicLabelsApp().run()
