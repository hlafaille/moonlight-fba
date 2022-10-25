import os

import pygame


class FzTkFontHandler:
    def __init__(self):
        self.button_font = pygame.font.Font(os.path.join("assets", "fonts", "pixelade.ttf"), 32)
        self.tooltip_font = pygame.font.Font(os.path.join("assets", "fonts", "pixelade.ttf"), 26)