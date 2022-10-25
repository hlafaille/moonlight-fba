from tk.Card import Card
from tk.Panel import Panel


class Welcome(Panel):
    def __init__(self):
        super().__init__(title="Welcome")

        # create cards
        self.test_card = Card(self)