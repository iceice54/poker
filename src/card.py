from enum import Enum

class Suit(Enum):
    DIAMONDS = "d"
    CLUBS = "c"
    HEARTS = "h"
    SPADES = "s"

class Card():
    def __init__(self, value: int, suit: Suit) -> None:
        self.value = value
        self.suit = suit
    
    def __str__(self) -> str:
        value_names = {
            11: "J",
            12: "Q",
            13: "K",
            14: "A"
        }
        value_name = value_names.get(self.value, str(self.value))
        return (f"{value_name}{self.suit.value}")
    
    def __lt__(self, other):
        return self.value < other.value
    
    def __eq__(self, other):
        if isinstance(other, Card):
            return self.value == other.value and self.suit == other.suit
        return False

    def __repr__(self):
        return f"Card(value={self.value}, suit={self.suit})"