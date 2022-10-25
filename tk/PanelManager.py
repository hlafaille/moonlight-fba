import logging

import pygame.font
from pygame import Surface


class PanelManager:
    """Controls which panel should be on screen, and which came before it"""
    def __init__(self, display: Surface, width: int, height: int):
        self._panels = []
        self.display = display
        self.width = width
        self.height = height
        self.fps = None
        self._current_panel = None

        # setup font objects
        self.font_title = pygame.font.Font("tk/fonts/font.ttf", 72)
        self.font_normal = pygame.font.Font("tk/fonts/regular.ttf", 32)

    def add(self, panel):
        """
        Adds a tracked panel
        :param panel:
        :return:
        """
        self._panels.append(panel)
        panel.set_manager(self)

        if len(self._panels) == 1:
            panel.focused = True

    def update(self, delta: float, fps: int):
        """
        Iterates over all panels, updates them if they're in focus
        :param delta:
        :return:
        """
        self.fps = fps

        for panel in self._panels:
            if panel.focused:
                panel.update(delta)