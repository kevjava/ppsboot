from textual.app import App, Binding, ComposeResult
from textual.containers import Container
from textual.widgets import Placeholder, TabbedContent, TabPane, Header, Footer
from ppsboot.dayswidget import DaysWidget

from ppsboot.log import LogWidget

class PPSBootCamp(App):
    """ The main app. """

    BINDINGS = [
        Binding("ctrl+q", "quit", "Quit", priority=False),
        Binding("ctrl+d", "show_tab('days')", "Days", priority=False),
        Binding("ctrl+c", "show_tab('code')", "Code", priority=False),
        Binding("ctrl+l", "show_tab('log')", "Log", priority=False),
    ]

    def compose(self) -> ComposeResult:
        """ Composes the app. """
        yield Header()
        yield Footer()
        
        self.rlog = LogWidget()

        with TabbedContent(id="tabs"):
            with TabPane(title="Days", id="days"):
                # yield Container(Placeholder("Days"))
                yield Container(DaysWidget())
            with TabPane(title="Code", id="code"):
                yield Container(Placeholder("Code"))
            with TabPane(title="Log", id="log"):
                yield self.rlog

    def action_quit(self) -> None:
        """ Quits the app. """
        self.exit()

    def action_show_tab(self, tab_name:str) -> None:
        """ Shows the tab with the given name. 
        
        Args: 
            tab_name (str): The name of the tab to show.
        """
        self.rlog.warn(f"Showing tab {tab_name}")
        tabs = self.get_child_by_id('tabs')
        self.rlog.debug(f"tabs: {tabs}")
        self.get_child_by_id('tabs').active = tab_name


if __name__ == "__main__":
    PPSBootCamp().run()