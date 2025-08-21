# A python program to shuffle a deck of cards
import random
import itertools

set_of_cards = list(itertools.product(range(1, 14), ['Hearts', 'Diamonds', 'Clubs', 'Spades']))
random.shuffle(set_of_cards)

print("Shuffled deck of cards:")
for card in range(10):
    rank, suit = set_of_cards[card]
    print(f"{rank} of {suit}")