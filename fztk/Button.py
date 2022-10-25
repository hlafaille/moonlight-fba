import pygame
from pygame.surface import Surface
from fztk.Color import FzTkPalette, FzTkColor
from fztk.FontHandler import FzTkFontHandler
from fztk.Widget import FzTkWidget


class FzTkButton(FzTkWidget):
    def __init__(self,
                 surface: Surface,
                 x: int,
                 y: int,
                 width: int,
                 height: int,
                 font_handler: FzTkFontHandler,
                 text="Button",
                 tooltip=None,
                 palette=FzTkPalette(primary=FzTkColor(245, 245, 245), complementary=FzTkColor(38, 50, 56))):

        # call superclass
        super().__init__(surface, x, y, width, height)

        # variables
        self._text = text.upper()
        self._tooltip = tooltip

        # set color palette
        self.set_palette(palette)

        # set font handler
        self.set_font_handler(font_handler)

    def set_text(self, text: str):
        self._text = str(text)

    def update(self):
        # call super to handle events
        super().update()

        # if the mouse is inside the widget, flip the colors
        if self.is_mouse_inside():
            bg = self.get_palette().get_complementary()
            text = self.get_palette().get_primary()
        else:
            bg = self.get_palette().get_primary()
            text = self.get_palette().get_complementary()

        # draw the rectangle to the screen
        pygame.draw.rect(
            self._surface, bg, pygame.Rect(
                self.get_position().x, self.get_position().y, self.get_size().width, self.get_size().height
            )
        )

        # draw the button text on screen
        button_text = self.get_font_handler().button_font.render(self._text, False, text)
        button_text_width = button_text.get_rect().width
        button_text_height = button_text.get_rect().height

        self._surface.blit(
            button_text,
            (
                self.get_position().x + (self.get_size().width / 2) - (button_text_width / 2),
                self.get_position().y + (self.get_size().height / 2) - (button_text_height / 2)
            )
        )

        # if a tooltip was provided, draw it when the mouse is inside
        if self._tooltip and self.is_mouse_inside():
            # render text
            tooltip_text = self.get_font_handler().tooltip_font.render(
                self._tooltip, False, (255, 255, 255), (0, 0, 0))
            tooltip_width = tooltip_text.get_rect().width

            # get mouse positions
            mouse_x = self.get_mouse_position().x
            mouse_y = self.get_mouse_position().y

            # todo change later
            window_width, window_height = 1920, 1080

            # if the tooltip will exit the screen bounds, blit it minus the tooltip width
            if tooltip_width + mouse_x > window_width:
                self._surface.blit(
                    tooltip_text,
                    ((mouse_x - tooltip_width) - (mouse_x - window_width),
                     mouse_y + 20)
                )
            else:
                self._surface.blit(
                    tooltip_text,
                    (mouse_x,
                     mouse_y + 20)
                )
