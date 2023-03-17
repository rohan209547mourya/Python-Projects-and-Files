"""
Types of Cards: Spades, Hearts, Diamonds, and Clubs

"""

from random import shuffle

values = {
    'Two': 2,
    'Three': 3,
    'Four': 4,
    'Five': 5,
    'Six': 6,
    'Seven': 7,
    'Eight': 8,
    'Nine': 9,
    'Ten': 10,
    'Jack': 11,
    'Queen': 12,
    'King': 13,
    'Ace': 14
}
suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
ranks = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']


class Card:

    def __init__(self, suit: str, rank: str):
        rank = rank.capitalize()
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit


class Deck:

    def __init__(self):
        self.all_cards = []

        for suite in suits:
            for rank in ranks:
                new_card = Card(suite, rank)
                self.all_cards.append(new_card)

    def shuffle_deck(self):
        shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()


class Player:

    def __init__(self, name):
        self.name = name
        self.cards = []

    def remove_one(self):
        return self.cards.pop(0)

    def add_cards(self, new_cards):
        # if type(new_cards) == type([]):
        if isinstance(new_cards, type([])):
            self.cards.extend(new_cards)
        else:
            self.cards.append(new_cards)

    def __str__(self):
        return f"Player {self.name} has {len(self.cards)} cards."


player_one = Player('Python')
player_two = Player('Java')

new_deck = Deck()
new_deck.shuffle_deck()

for card in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

is_game_one = True
round_number = 0

while is_game_one:
    round_number += 1
    print(f'Round {round_number}')

    if len(player_one.cards) == 0:
        print(f'{player_one.name}, out of cards! {player_two.name} Wins!')
        is_game_one = False
        break

    if len(player_two.cards) == 0:
        print(f'{player_two.name}, out of cards! {player_one.name} Wins!')
        is_game_one = False
        break

    player_one_cards = [player_one.remove_one()]
    player_two_cards = [player_two.remove_one()]

    at_war = True

    while at_war:
        if player_one_cards[-1].value > player_two_cards[-1].value:
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)
            at_war = False

        elif player_two_cards[-1].value > player_one_cards[-1].value:
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)
            at_war = False

        else:
            print("WAR!")
            if len(player_one.cards) < 10:
                print(f"{player_one.name} is unable to declare a war!")
                print(f"🎉🎉{player_two.name} Wins the game!🎉🎉")
                is_game_one = False
                break

            elif len(player_two.cards) < 10:
                print(f"{player_two.name} is unable to declare a war!")
                print(f"🎉🎉{player_one.name} Wins the game!🎉🎉")
                is_game_one = False
                break

            else:
                for nums in range(5):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())


