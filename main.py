import os

import pygame

from fztk.Button import FzTkButton
from fztk.FontHandler import FzTkFontHandler

# width and height
WIDTH = 1280
HEIGHT = 720

# initialize pygame and create screen
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Faction: Zero")


# create FzEngine objects
font_handler = FzTkFontHandler()
clock = pygame.time.Clock()


#button.register_click_callback(lambda: scene_handler.dev_toggle_scene())

if __name__ == "__main__":
    print("Getting screen sizes")
    WIDTH = int(os.system("cat /sys/class/graphics/fb0/virtual_size | cut -d, -f1"))
    HEIGHT = int(os.system("cat /sys/class/graphics/fb0/virtual_size | cut -d, -f2"))

    # create button
    button = FzTkButton(
        font_handler=font_handler,
        x=int(WIDTH - 180),
        y=0,
        height=60,
        width=180,
        surface=screen,
        text="Toggle Scene",
        tooltip="Changes between development engine scenes."
    )

    while True:
        delta_time = clock.tick(60) / 1000

        button.set_text("ass")
        button.update()

        pygame.display.update()
