import pytest
from src.hand import Hand, PlayerHand, CommunityCards
from src.card import Card, Suit

def test_initialization() -> None:
    hand = Hand()
    assert len(hand.cards) == 0

def test_add_card() -> None:
    hand = Hand()
    hand.add_card(Card(4, Suit.HEARTS))
    assert len(hand.cards) == 1

def test_exceed_player_hand() -> None:
    playerhand = PlayerHand()
    playerhand.add_card(Card(4, Suit.HEARTS))
    playerhand.add_card(Card(5, Suit.DIAMONDS))
    with pytest.raises(ValueError):
        playerhand.add_card(Card(10, Suit.DIAMONDS))

def test_exceed_community_cards() -> None:
    community_cards = CommunityCards()
    cards = [Card(i, Suit.HEARTS) for i in range(2, 7)]
    for card in cards:
        community_cards.add_card(card)
    with pytest.raises(ValueError):
        community_cards.add_card(Card(10, Suit.DIAMONDS))

def test_str() -> None:
    hand = Hand()
    hand.add_card(Card(3, Suit.CLUBS))
    hand.add_card(Card(4, Suit.DIAMONDS))