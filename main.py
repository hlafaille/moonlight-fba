import pygame

from fztk.Button import FzTkButton
from fztk.FontHandler import FzTkFontHandler

# width and height
WIDTH = 1920
HEIGHT = 1080

# initialize pygame and create screen
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Faction: Zero")


# create FzEngine objects
font_handler = FzTkFontHandler()

clock = pygame.time.Clock()

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

#button.register_click_callback(lambda: scene_handler.dev_toggle_scene())

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    delta_time = clock.tick(60) / 1000

    button.set_text("ass")
    button.update()

    pygame.display.update()
