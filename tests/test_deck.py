from src.deck import Deck
from src.card import Card

def test_initialization() -> None:
    deck = Deck()
    assert len(deck.cards) == 52

def test_deal() -> None:
    deck = Deck()
    dealt_card = deck.deal_card()
    assert isinstance(dealt_card, Card)

def test_str() -> None:
    deck = Deck()
    deck_str = str(deck)
    assert len(deck_str) > 0
    assert len(deck_str.split(", ")) == 52 

def test_len() -> None:
    deck = Deck()
    assert len(deck) == 52