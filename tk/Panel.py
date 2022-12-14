from typing import Optional
import pygame
from pygame import Color
from tk.PanelManager import PanelManager


class Panel:
    """A basic container object for all UI objects
    Thinking in terms of Xbox Series S/X UI styling, a significant portion of the UI runs in full screen mode or
    near full screen mode. This UI system will follow the same philosophy
    """

    def __init__(self, title="Panel", subtitle: Optional[str] = None, focused=False):
        self.manager: Optional[PanelManager] = None
        self.title_bar: Optional[PanelTitle] = None

        self.title = title
        self.subtitle = subtitle
        self.focused = focused
        self.id = id(self)
        self.cards = []

    def set_manager(self, manager: PanelManager):
        """
        Sets the PanelManager for this object, and initializes the title bar object
        :param manager:
        :return:
        """
        self.manager = manager
        self.title_bar = PanelTitle(manager=self.manager, title=self.title, subtitle=self.subtitle)

    def add_card(self, card):
        """
        Adds a widget to this panel
        :param widget:
        :return:
        """
        self.cards.append(card)

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
        self.manager.display.fill(Color("#272727"))
        self.title_bar.update()

        for card in self.cards:
            card.update(float)

    def get_drawable_area(self) -> tuple:
        """
        Returns a set of coordinates that are acceptable to be drawn in
        :return:
        """
        return (0, 140), (self.manager.width, self.manager.height)


class PanelTitle:
    """The title bar for a panel object"""
    def __init__(self, manager: PanelManager, title="Panel", subtitle: Optional[str] = None):
        self.manager = manager
        self.title = title
        self.subtitle = subtitle

    def get_size(self) -> tuple:
        """
        Returns the size of the title bar
        :return:
        """
        return self.manager.width, 140

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

        # if there's a subtitle, draw it
        if self.subtitle:
            subtitle = self.manager.font_subtitle.render(self.subtitle, True, Color("#c2c2c2"))
            subtitle_rect = subtitle.get_bounding_rect()

            # blit title text
            title_y = title_rect.height - subtitle_rect.height - subtitle_rect.y - 2
            title_y = (title_y + 140 / 2) - (title_rect.height / 2)
            self.manager.display.blit(subtitle, (title_rect.width + 40, title_y))
