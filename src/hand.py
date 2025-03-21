from __future__ import annotations
from typing import TYPE_CHECKING
from .utils import cards_to_str

if TYPE_CHECKING:
    from .card import Card

class Hand():
    def __init__(self, max_cards: int = 2, cards: list[Card] | None = None) -> None:
        self.cards = cards if cards is not None else []
        self.max_cards = max_cards

    def add_card(self, card: Card) -> None:
        if len(self.cards) >= self.max_cards:
            raise ValueError("A hand cannot have more than 2 cards")
        self.cards.append(card)

    def __str__(self) -> str:
        return cards_to_str(self.cards)
    
    def __len__(self) -> int:
        return len(self.cards)

class PlayerHand(Hand):
    def __init__(self, cards: list[Card] | None = None) -> None:
        super().__init__(2, cards)


class CommunityCards(Hand):
    def __init__(self, cards: list[Card] | None = None) -> None:
        super().__init__(5, cards)
