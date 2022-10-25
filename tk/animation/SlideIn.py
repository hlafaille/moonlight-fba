class SlideIn:
    def __init__(self, duration=1, exponent=2.7):
        self.duration = duration
        self.exponent = exponent
        self._objects = []

    def add(self):
