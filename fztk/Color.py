"""
FZTk Color class:
-----
This class simply represents an RGB color value
"""
import pygame


class FzTkColor:
    def __init__(self, red: int, green: int, blue: int):
        self.red = red
        self.green = green
        self.blue = blue

    def get_tuple(self):
        return self.red, self.green, self.blue


"""
FZTk Palette class:
-----
This class represents a main and opposite color (for example, a buttons main color, and a buttons highlight color)
"""


class FzTkPalette:
    def __init__(self, primary: FzTkColor, complementary=None):
        self.primary = primary
        self.complementary = complementary
        self._range = []
        self._break_range = False

        # if no complementary was provided, calculate complementary color
        if not complementary:
            r, g, b = self.primary.get_tuple()
            x, y, z = self._complement(r, g, b)
            self.complementary = FzTkColor(x, y, z)

    def get_primary(self) -> tuple:
        return self.primary.get_tuple()

    def get_complementary(self) -> tuple:
        return self.complementary.get_tuple()

    def get_range(self):
        return self._range

    def reset_break_range(self):
        self._break_range = False

    def apply_range_to_object(self, object_to_color):
        for element, color in enumerate(list(reversed(self._range))):
            # if we're not at the last element in this range, update the objects color
            if element < len(self._range) and not self._break_range:
                object_to_color.set_color(color)
            else:
                break
        else:
            self._break_range = True

    # returns a list of tuples that contain data to fade between the two colors
    def get_range(self):
        reds = []
        greens = []
        blues = []

        # reset the ranges list
        self._range = []

        # calculate how far we have to go between the two reds
        red_steps = round(abs(self.primary.red - self.complementary.red) / 60)

        # sort the two red values so we can have the smallest first for range()
        if self.primary.red > self.complementary.red:
            beginning = self.complementary.red
            ending = self.primary.red
        else:
            beginning = self.primary.red
            ending = self.complementary.red

        # step from primary red to complementary red
        for x in range(beginning, ending, red_steps):
            reds.append(x)

        # calculate how far we have to go between the two green
        green_steps = round(abs(self.primary.green - self.complementary.green) / 60)

        # sort the two green values so we can have the smallest first for range()
        if self.primary.green > self.complementary.green:
            beginning = self.complementary.green
            ending = self.primary.green
        else:
            beginning = self.primary.green
            ending = self.complementary.green

        # step from primary green to complementary green
        for x in range(beginning, ending, green_steps):
            greens.append(x)

        # calculate how far we have to go between the two blue
        blue_steps = round(abs(self.primary.blue - self.complementary.blue) / 60)

        # sort the two blue values so we can have the smallest first for range()
        if self.primary.blue > self.complementary.blue:
            beginning = self.complementary.blue
            ending = self.primary.blue
        else:
            beginning = self.primary.blue
            ending = self.complementary.blue

        # step from primary blue to complementary blue
        for x in range(beginning, ending, blue_steps):
            blues.append(x)

        # enumerate over the red values, set the objects color
        for element, red in enumerate(reds):
            try:
                r = red
            except IndexError:
                r = reds[-1]

            try:
                g = greens[element]
            except IndexError:
                g = greens[-1]

            try:
                b = blues[element]
            except IndexError:
                b = blues[-1]

            self._range.append((r, g, b))

    # Sum of the min & max of (a, b, c)
    def _hilo(self, a, b, c):
        if c < b: b, c = c, b
        if b < a: a, b = b, a
        if c < b: b, c = c, b
        return a + c

    def _complement(self, r, g, b):
        k = self._hilo(r, g, b)
        return tuple(k - u for u in (r, g, b))
