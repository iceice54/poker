from __future__ import annotations

from .card import Card

def cards_to_str(cards: list[Card]):
    return ", ".join(str(card) for card in cards)