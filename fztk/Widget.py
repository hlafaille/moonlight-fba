"""
FzTkWidget:
-----
The base widget class for FzTk. This class handles all common functions between widgets like setting and getting
positions and sizes, setting colors, etc. FzTkWidget (and its accompanying subclassed widgets) are designed to provide
the best developer experience while being powerful.
"""
import pygame.mouse
from pygame.surface import Surface

from fztk.Color import FzTkPalette
from fztk.Exceptions import NoPaletteException, RegisterCallbackException
from fztk.FontHandler import FzTkFontHandler


class FzTkWidget:
    def __init__(self,
                 surface: Surface,
                 x: int,
                 y: int,
                 width: int,
                 height: int,
                 pane=None):

        # general variables / refs
        self._surface = surface
        self._x = x
        self._y = y
        self._width = width
        self._height = height
        self._parent = pane
        self._palette = None
        self._font_handler = None

        # callbacks
        self._click_callbacks = []

    # sets the position for this widget
    def set_position(self, x: int, y: int):
        self._x = int(x)
        self._y = int(y)

    # returns the x and y position for this widget
    def get_position(self):
        return FzTkCoordinate(self._x, self._y)

    # sets the size of this widget
    def set_size(self, width: int, height: int):
        self._width = int(width)
        self._height = int(height)

    # returns the width and height of this widget
    def get_size(self):
        return FzTkSize(self._width, self._height)

    # returns the mouse position
    def get_mouse_position(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        return FzTkCoordinate(mouse_x, mouse_y)

    # returns a bool if the mouse is inside the defined size of this widget
    def is_mouse_inside(self):
        if (self.get_mouse_position().x in range(self._x, self._width + self._x)) and (
                self.get_mouse_position().y in range(self._y, self._height + self._y)):
            return True
        else:
            return False

    # returns if mouse1 (left click) is down
    def is_mouse1_down(self):
        m1, scroll, m2 = pygame.mouse.get_pressed(3)
        if m1 and self.is_mouse_inside():
            return True
        else:
            return False

    # sets the layout pane for this widget
    def set_pane(self, pane):
        self._parent = pane

    # registers a callback function for when this widget is clicked
    def register_click_callback(self, function):
        if callable(function):
            self._click_callbacks.append(FzTkCallback(function))
        else:
            raise RegisterCallbackException(
                f"'{function}' is not a callable function, therefore it can not be registered as a callback.")

    # sets the palette for this widget
    def set_palette(self, palette: FzTkPalette):
        self._palette = palette

    # returns the palette for this widget
    def get_palette(self) -> FzTkPalette:
        if self._palette:
            return self._palette
        raise NoPaletteException("An FzTkWidget attempted to retrieve a FzTkPalette that has not been set.")

    # sets the widget font handler
    def set_font_handler(self, font_handler: FzTkFontHandler):
        self._font_handler = font_handler

    # returns the font handler
    def get_font_handler(self) -> FzTkFontHandler:
        return self._font_handler

    # updates this widget
    def update(self):
        # if there's any callbacks and M1 is down, call the callbacks
        if len(self._click_callbacks) > 0 and self.is_mouse1_down():
            # iterate over all the callbacks, call them if they haven't been called
            for callback in self._click_callbacks:
                if not callback.called:
                    callback.function()
                    callback.called = True

        # if theres any callbacks and M1 is not down, reset all callback "called" variables
        if len(self._click_callbacks) > 0 and not self.is_mouse1_down():
            for callback in self._click_callbacks:
                callback.called = False

class FzTkCoordinate:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __iter__(self):
        return self.x, self.y


class FzTkSize:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def __iter__(self):
        return self.width, self.height


class FzTkCallback:
    def __init__(self, function, called=False):
        self.function = function
        self.called = called
