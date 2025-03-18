from enum import Enum
from typing import TYPE_CHECKING

from .hand import PlayerHand, CommunityCards
from .card import Card

class Evaluator():

    def calc_hand_strength(self, player_hand: PlayerHand, community_cards: CommunityCards):
        all_cards = player_hand.cards + community_cards.cards
        def check_flush(cards) -> list[Card]:
            suits = [card.suit.value for card in cards]
            print(suits)
            for suit in ["d", "c", "h", "s"]:
                if suits.count(suit) >= 5:
                    res = sorted([str(card) for card in cards if card.suit.value == suit])
                    return res

        def check_straight(cards) -> list[Card]:
            values = [card.value for card in cards]
            print(values)
            values = sorted(set(values))
            if 14 in values:
                values.insert(0,1)
            print(values)
            for i in range(len(values)-4):
                if values[len(values)-1-i] - values[len(values)-5-i] == 4:
                    print("Straight")
            
        print(check_flush(all_cards))
        # check_straight(all_cards)
        #Royal Flush

        #Straight Flush

        #Four of a kind

        #Full house

        #Flush

        #Straight

        #Three of a kind

        #Two pair

        #Pair

        #High Card