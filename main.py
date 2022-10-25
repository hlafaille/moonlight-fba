import pygame

from tk.Panel import Panel
from tk.PanelManager import PanelManager

# width and height
WIDTH = 1920
HEIGHT = 1080

# initialize pygame and create screen
pygame.init()
display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.mouse.set_visible(False)

# create clock
clock = pygame.time.Clock()

# create panel manager & main panel
panel_manager = PanelManager(display)
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
