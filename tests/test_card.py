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

def test_lt() -> None:
    card1 = Card(10, Suit.HEARTS)
    card2 = Card(5, Suit.DIAMONDS)
    assert card1 > card2

    card3 = Card(12, Suit.HEARTS)
    assert card1 < card3

def test_eq() -> None:
    card1 = Card(10, Suit.HEARTS)
    card2 = Card(10, Suit.HEARTS)
    assert card1 == card2

    card3 = Card(10, Suit.CLUBS)
    card4 = Card(9, Suit.HEARTS)
    assert card1 != card3
    assert card1 != card4

    assert card1 != 10

def test_repr() -> None:
    card = Card(10, Suit.HEARTS)
    assert card.__repr__() == "Card(value=10, suit=Suit.HEARTS)"