from src.card import Card, Suit

def test_initialization() -> None:
    card = Card(10, Suit.CLUBS)
    assert card.value == 10
    assert card.suit == Suit.CLUBS

def test_str() -> None:
    card1 = Card(5, Suit.HEARTS)
    assert str(card1) == "5h"
    card2 = Card(14, Suit.DIAMONDS)
    assert str(card2) == "Ad"