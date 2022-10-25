import pygame

from fztk.Button import FzTkButton
from fztk.FontHandler import FzTkFontHandler

# width and height
WIDTH = 1920
HEIGHT = 1080

# initialize pygame and create screen
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Faction: Zero")
pygame.mouse.set_visible(False)

# create FzEngine objects
font_handler = FzTkFontHandler()

clock = pygame.time.Clock()

# create button
button = FzTkButton(
    font_handler=font_handler,
    x=0,
    y=0,
    height=60,
    width=180,
    surface=screen,
    text="Toggle Scene",
    tooltip="Changes between development engine scenes."
)

# main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    delta_time = clock.tick(60) / 1000

    button.set_text(round(clock.get_fps()))
    button.update()

    pygame.display.update()
