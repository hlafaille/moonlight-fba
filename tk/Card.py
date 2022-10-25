import pygame
from pygame import surface
from pygame.color import Color

from tk.Panel import Panel


class Card:
    """A card-like container that can contain other widgets"""
    def __init__(self, panel: Panel):
        self.panel = panel
        self.panel.add_card(self)

        self.width = 900
        self.height = 700

    def update(self, delta: float):
        """
        Called from the parent panel, draws ourselves
        :return:
        """

        # calculate center of screen
        begin, end = self.panel.get_drawable_area()

        card_x = end[0] / 2 - self.width / 2
        card_y = end[1] / 2 - self.height / 2 + begin[1] / 2

        pygame.draw.rect(self.panel.manager.display, Color("#363636"), pygame.Rect(card_x, card_y, self.width, self.height))