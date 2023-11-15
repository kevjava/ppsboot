from textual.app import App, ComposeResult
from textual.widgets import Placeholder

class MyApp(App):

    def compose(self) -> ComposeResult:
        yield Placeholder("Hello, world!")

if __name__ == "__main__":
    MyApp().run()