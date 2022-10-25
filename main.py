import os
import subprocess
import sys

import pygame

from tk.Panel import Panel
from tk.PanelManager import PanelManager

# width and height
if sys.platform == "linux":
    FB_VIRTUAL_SIZE = subprocess.run(["cat", "/sys/class/graphics/fb0/virtual_size"], stdout=subprocess.PIPE)
    WIDTH, HEIGHT = FB_VIRTUAL_SIZE.stdout.decode("utf8").split(",")
    WIDTH = int(WIDTH)
    HEIGHT = int(HEIGHT)
else:
    WIDTH = 1920
    HEIGHT = 1080

# initialize pygame and create screen
pygame.init()
pygame.joystick.init()
display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.mouse.set_visible(False)

# create clock
clock = pygame.time.Clock()

# create panel manager & main panel
panel_manager = PanelManager(display, WIDTH, HEIGHT)
panel = Panel("Welcome")
panel_manager.add(panel)

# main loop
while True:
    # check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # run clock
    delta = clock.tick(60) / 1000

    panel_manager.update(delta)

    # update display
    pygame.display.update()
