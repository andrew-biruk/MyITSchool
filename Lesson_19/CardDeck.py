# Implement a card deck iterator (52 cards) CardDeck.
# Each card is represented as a string "2 of Spades".
# When next() is called, the next card is shown.
# When iteration is over, a StopIteration error occurs.

from time import sleep
from random import shuffle


class CardDeck:
    def __init__(self):
        self.deck = [f"{v} of {s}"
                     for v in "2 3 4 5 6 7 8 9 10 Jack Queen King Ace".split(" ")
                     for s in ["Clubs", "Diamonds", "Hearts", "Spades"]]
        shuffle(self.deck)

    def __iter__(self):
        return self

    def __next__(self):
        if self.deck:
            return self.deck.pop()
        else:
            raise StopIteration


deck1 = CardDeck()

# [print(c) for c in deck1]        # N of iterations can be limited by deck size
for _ in range(53):                # or can exceed N of cards to raise exception
    sleep(0.25)
    print(next(deck1))
