from textual.widgets import Static, RichLog, Footer
from textual.app import Binding, ComposeResult

from rich.text import Text

class LogWidget(Static):


    BINDINGS = [
        Binding("ctrl+x", "clear", "Clear", priority=True),
    ]

    def compose(self) -> ComposeResult:
        self._log = RichLog(highlight=True, markup=True)
        yield self._log

    def action_clear(self) -> None:
        """ Clears the log. """
        self._log.clear()
    
    def on_show(self) -> None:
        """ Called when the widget is shown. """
        self._log.focus(self)

    def debug(self, msg:str) -> None:
        """ Logs a debug message. """
        self._log.write( Text.assemble( ("DEBUG", "bold blue"), ": ", msg,))

    def info(self, msg:str) -> None:
        """ Logs an info message. """
        self._log.write( Text.assemble( ("INFO", "bold"), ": ", msg,))
    
    def warn(self, msg:str) -> None:
        """ Logs a warning message. """
        self._log.write( Text.assemble( ("WARN", "bold yellow"), ": ", msg,))
    
    def error(self, msg:str) -> None:
        """ Logs an error message. """
        self._log.write( Text.assemble( ("ERROR", "bold red"), ": ", msg,))