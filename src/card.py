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