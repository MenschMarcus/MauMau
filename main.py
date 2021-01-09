################################################################################
# LIBS
################################################################################

import random
import sys


################################################################################
# CONSTANTS
################################################################################

CARDS = [ # 7, 8, 9, 1(0), U(nter), O(ber), A(ss)
    "S7", "S8", "S9", "S1", "SU", "SO", "SK", "SA", # Schell
    "H7", "H8", "H9", "H1", "HU", "HO", "HK", "HA", # Herz
    "B7", "B8", "B9", "B1", "BU", "BO", "BK", "BA", # Blatt
    "E7", "E8", "E9", "E1", "EU", "EO", "EK", "EA", # Eichel
]

PLAYERS = ["Hans", "Lena", "Paul", "Anna"]

NUM_CARDS_PER_PLAYER = 6


################################################################################
# CLASSES
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

################################################################################

class Card:

    def __init__(self, name):
        self.color = name[0]
        self.value = name[1]

    def get_color(self):
        return self.color

    def get_value(self):
        return self.value

    def get_name(self):
        return self.color+self.value


################################################################################

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


################################################################################
# PROGRAM
################################################################################

# init players
players = []

for player_name in PLAYERS:
    players.append(Player(player_name))

# init piles
draw_pile = Pile()
drop_pile = Pile()

# init cards and put on draw pile
for card_name in CARDS:
    new_card = Card(card_name)
    draw_pile.drop(new_card)
    # print(new_card.get_color(), new_card.get_value())

draw_pile.shuffle()

# distribute cards among players
for player in players:
    for it in range(0, NUM_CARDS_PER_PLAYER):
        new_card = draw_pile.draw()
        player.draw_card(new_card)

# init drop pile = put start card from draw pile
start_card = draw_pile.draw()
drop_pile.drop(start_card)

print("Game starts with card:", start_card.get_name())

game_is_over = False # status variable: has a player already won the game?

turn_it = 0
while not game_is_over:

    # determine current player
    # -> get turn_it (number of turn)
    # -> modulo number of players
    # => ensures first player's turn after last player
    current_player = players[turn_it % len(players)]

    # determine current card to play
    current_card = drop_pile.show_upper_card()

    # player: check for each card if it matches the start card
    player_has_matching_card = False
    for hand_card in current_player.get_hand():
        if hand_card.get_color() == current_card.get_color() or hand_card.get_value() == current_card.get_value():
            current_player.play_card(hand_card)
            drop_pile.drop(hand_card)
            print("Player", current_player.get_name(), "plays card", hand_card.get_name())
            player_has_matching_card = True

            if current_player.get_num_cards() == 1:
                print("Player", current_player.get_name(), "MAU!")

            # test: is player winning the game?
            elif current_player.get_num_cards() == 0:
                game_is_over = True
                print("Player", current_player.get_name(), "MAU MAU! and has won the game")

            break

    # if no matching card => draw new card
    if not player_has_matching_card:
        new_card = draw_pile.draw()
        current_player.draw_card(new_card)
        print("Player", current_player.get_name(), "draws card")

        # if draw pile is empty
        if draw_pile.get_size() == 0:
            last_card = drop_pile.draw()
            drop_pile.shuffle()
            draw_pile = drop_pile
            drop_pile = Pile()
            drop_pile.drop(last_card)
            print("draw pile empty -> re-shuffle!")

    turn_it += 1


# print(draw_pile.draw().get_color())
