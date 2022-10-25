from typing import Optional

from pygame import Color

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

        title = self.manager.font_title.render(self.title, True, Color("#f5f5f5"))
        subtitle = self.manager.font_normal.render("Hello, world!", True, Color("#bdbdbd"))
        self.manager.display.fill(Color("#212121"))
        self.manager.display.blit(title, (20, 20))
        self.manager.display.blit(subtitle, (330, 56))
