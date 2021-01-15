class Player:

    def __init__(self, name=""):
        self.name = name
        self.hand = []

    def play(self, card):
        self.hand.remove(card)

    def draw(self, card):
        self.hand.append(card)

    def get_name(self):
        return self.name

    def get_num_cards(self):
        return len(self.hand)

    def get_hand(self):
        return self.hand

    def print_hand(self):
        it = 1
        for card in self.hand:
            print("")
            card.print_card(it)
            it += 1
