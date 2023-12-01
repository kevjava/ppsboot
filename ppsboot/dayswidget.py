from textual.widgets import Static, Label
from textual.app import ComposeResult

class DaysWidget(Static):
    """ A widget that displays the days. """

    def compose(self) -> ComposeResult:
        """ Composes the widget. """
        yield Label("Days")