from typing import Optional

import pygame
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

    def _draw_title(self):
        """
        Draws the title at the top of the screen, returns the rect dimmensions
        :return:
        """
        title_bar = pygame.draw.rect(self.manager.display, Color("#1c1c1c"), pygame.Rect(0, 0, self.manager.width, 140))
        title = self.manager.font_title.render(self.title, True, Color("#f5f5f5"))
        self.manager.display.blit(title, (20, 25))

    def update(self, delta: float):
        """
        Called from the panel manager, draws this panel
        :param delta:
        :return:
        """
        self.manager.display.fill(Color("#272727"))
        for widget in self.widgets:
            widget.update(delta)
        self._draw_title()
