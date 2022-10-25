"""
FZTkPane:
-----
This class acts as a container to hold a group of FZTk Widgets. It can handle automatic resizing and positioning
of widgets within it, along with triggering those widgets update functions.
"""

POSITION_VH_CENTER = 1


class FZTkPane:
    def __init__(self):
        self._widgets = []

    # adds a widget to the pane
    def add_widget(self, widget, position_mode=0):
        self._widgets.append({"widget": widget, "position_mode": position_mode})

    #
    def update(self):

