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
        self.title_bar: Optional[PanelTitle] = None

        self.title = title
        self.focused = focused
        self.id = id(self)
        self.widgets = []

    def set_manager(self, manager: PanelManager):
        """
        Sets the PanelManager for this object, and initializes the title bar object
        :param manager:
        :return:
        """
        self.manager = manager
        self.title_bar = PanelTitle(manager=self.manager, title=self.title)

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

    def _slide_in(self, delta: float):
        """
        Function that draws the slide_in animation
        :return:
        """


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
        self.manager.display.fill(Color("#272727"))
        for widget in self.widgets:
            widget.update(delta)
        self.title_bar.update()


class PanelTitle:
    """The title bar for a panel object"""
    def __init__(self, manager: PanelManager, title="Panel"):
        self.manager = manager
        self.title = title

    def update(self):
        """
        Called from the panel, draws this title bar
        :return:
        """

        # create title text
        title_text = self.manager.font_title.render(self.title, True, Color("#f5f5f5"))
        title_rect = title_text.get_bounding_rect()

        # draw the title bar
        title_bar = pygame.draw.rect(
            self.manager.display,
            Color("#1c1c1c"),
            pygame.Rect(0, 0, self.manager.width, 140)
        )

        # blit title text
        title_y = 0 - title_rect.y
        title_y = (title_y + 140 / 2) - (title_rect.height / 2)
        self.manager.display.blit(title_text, (10, title_y))
