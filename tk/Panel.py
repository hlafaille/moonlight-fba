from typing import Optional

from tk.PanelManager import PanelManager


class Panel:
    """A basic container object for all UI objects
    Thinking in terms of Xbox Series S/X UI styling, a significant portion of the UI runs in full screen mode or
    near full screen mode. This UI system will follow the same philosophy
    """

    def __init__(self, title="Panel", focused=False):
        self.manager: Optional[PanelManager] = None
        self.title = title
        self.focused = focused
        self.id = id(self)
        self.widgets = []

    def add(self, widget):
        """
        Adds a widget to this panel
        :param widget:
        :return:
        """
        self.widgets.append(widget)

    def set_focus(self, focus: bool):
        """
        Sets this panel in focus
        :param focus:
        :return:
        """
        self.focused = focus

    def _close(self):
        """
        Closes this panel
        :return:
        """

    def update(self, delta: float):
        """
        Called from the panel manager, draws this panel
        :param delta:
        :return:
        """
        for widget in self.widgets:
            widget.update(delta)

        text = self.manager.font_title.render(self.title, True, (255, 255, 255))
        self.manager.display.blit(text, (0, 0))
