from src.card import Card, Suit
from src.utils import cards_to_str

def test_cards_to_str() -> None:
    cards = [
        Card(10, Suit.HEARTS),
        Card(11, Suit.DIAMONDS),
        Card(12, Suit.CLUBS)
    ]
    assert cards_to_str(cards) == "10h, Jd, Qc"

def test_cards_to_str_empty_list() -> None:
    cards = []
    assert cards_to_str(cards) == ""

def test_cards_to_str_single_card() -> None:
    cards = [Card(14, Suit.SPADES)]
    assert cards_to_str(cards) == "As"