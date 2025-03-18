import random
from .card import Card, Suit
from .utils import cards_to_str

class Deck():
    def __init__(self) -> None:
        self.cards = []
        self._create_shuffled_deck()

    def _create_shuffled_deck(self) -> None:
        for value in range(2,15):
            for suit in Suit:
                self.cards.append(Card(value, suit))
        random.shuffle(self.cards)

    def deal_card(self) -> Card:
        return self.cards.pop()

    def __str__(self) -> str:
        return cards_to_str(self.cards)
    
    def __len__(self) -> int:
        return len(self.cards)