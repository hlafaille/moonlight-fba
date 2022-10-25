import logging

import pygame.font
from pygame import Surface
from rich.logging import RichHandler


class PanelManager:
    """Controls which panel should be on screen, and which came before it"""
    def __init__(self, display: Surface):
        self._panels = []
        self.display = display
        self._current_panel = None

        # setup rich logger
        logging.basicConfig(
            level="NOTSET",
            format="%(message)s",
            datefmt="[%X]",
            handlers=[RichHandler(rich_tracebacks=True)]
        )
        self.logger = logging.getLogger("rich")

        # setup font objects
        self.font_title = pygame.font.Font("tk/fonts/roboto_regular.ttf", 48)

    def add(self, panel):
        """
        Adds a tracked panel
        :param panel:
        :return:
        """
        self._panels.append(panel)
        panel.manager = self

        if len(self._panels) == 1:
            panel.focused = True

    def update(self, delta: float):
        """
        Iterates over all panels, updates them if they're in focus
        :param delta:
        :return:
        """
        for panel in self._panels:
            if panel.focused:
                panel.update(delta)