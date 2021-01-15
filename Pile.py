import random


################################################################################
class Pile:

    def __init__(self):
        self.cards = []

    def drop(self, card):
        self.cards.append(card)

    def draw(self):
        return self.cards.pop()

    def show_upper_card(self):
        return self.cards[-1]

    def shuffle(self):
        random.shuffle(self.cards)

    def get_size(self):
        return len(self.cards)
