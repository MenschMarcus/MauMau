class Player:

    def __init__(self, name=""):
        self.name = name
        self.hand = []

    def play_card(self, card):
        self.hand.remove(card)

    def draw_card(self, card):
        self.hand.append(card)

    def skip(self):
        pass

    def get_name(self):
        return self.name

    def get_num_cards(self):
        return len(self.hand)

    def get_hand(self):
        return self.hand
