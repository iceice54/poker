from enum import Enum
from typing import TYPE_CHECKING

from .hand import PlayerHand, CommunityCards
from .card import Card

class HandStrength(Enum):
    ROYAL_FLUSH = 10
    STRAIGHT_FLUSH = 9
    FOUR_OF_A_KIND = 8
    FULL_HOUSE = 7
    FLUSH = 6
    STRAIGHT = 5
    THREE_OF_A_KIND = 4
    TWO_PAIR = 3
    PAIR = 2
    HIGH_CARD = 1

class Evaluator():

    def check_flush(self, cards: list[Card]) -> list[Card] | None:
            suits = [card.suit.value for card in cards]
            for suit in ["d", "c", "h", "s"]:
                if suits.count(suit) >= 5:
                    return [card for card in cards if card.suit.value == suit]
            return None
    
    def check_straight(self, cards: list[Card]) -> list[Card] | None:
            values = sorted(set(card.value for card in cards), reverse=True)
            if 14 in values:
                values.insert(0,1)
            for i in range(len(values)-4):
                if values[i] - values[i+4] == 4:
                    return [card for card in cards if card.value in values[i:i + 5]]
            return None

    def calc_hand_strength(self, player_hand: PlayerHand, community_cards: CommunityCards) -> tuple[HandStrength, list[Card]]:
        # all_cards: list[Card] = player_hand.cards + community_cards.cards
        sorted_by_value_decreasing: list[Card] = sorted(player_hand.cards + community_cards.cards, reverse=True)
        values = [card.value for card in sorted_by_value_decreasing]
        flush_cards = self.check_flush(sorted_by_value_decreasing)

        if flush_cards:
            straight_flush_cards = self.check_straight(flush_cards)
            if straight_flush_cards:
                if max(card.value for card in straight_flush_cards) == 14:
                    #Royal Flush
                    print("Royal Flush")
                    return (HandStrength.ROYAL_FLUSH, straight_flush_cards)
                else:
                    #Straight Flush
                    print("Straight Flush")
                    return (HandStrength.STRAIGHT_FLUSH, straight_flush_cards)
        trips = set()
        pairs = set()
        print(sorted_by_value_decreasing)
        for value in values:
            #Four of a kind
            if values.count(value) == 4:
                print("foak")
                res = [card for card in sorted_by_value_decreasing if card.value == value]
                if sorted_by_value_decreasing[0].value == value:
                    res.append(sorted_by_value_decreasing[4])
                else:
                    res.append(sorted_by_value_decreasing[0])
                return (HandStrength.FOUR_OF_A_KIND, res)
            elif values.count(value) == 3:
                trips.add(value)
            elif values.count(value) == 2:
                pairs.add(value)
        if len(trips) == 2:
            #Full house
            res = [card for card in sorted_by_value_decreasing if card.value in trips]
            res.pop()
            return (HandStrength.FULL_HOUSE, res)
        elif len(trips) == 1 and len(pairs) >= 1:
            res = [card for card in sorted_by_value_decreasing if card.value in trips]
            res = res + [card for card in sorted_by_value_decreasing if card.value == max(pairs)]
            return (HandStrength.FULL_HOUSE, res)

        #Flush
        if flush_cards:
            return (HandStrength.FLUSH, flush_cards)
        #Straight
        straight_cards = self.check_straight(sorted_by_value_decreasing)
        if straight_cards:
            return (HandStrength.STRAIGHT, straight_cards)
        #Three of a kind
        if trips:
            high = max(trips)
            res = [card for card in sorted_by_value_decreasing if card.value == high]
            for card in sorted_by_value_decreasing:
                if card.value != high:
                    res.append(card)
                if len(res) == 5:
                    break
            return (HandStrength.THREE_OF_A_KIND, res)
        #Two pair
        if len(pairs) >= 2:
            high1 = max(pairs)
            pairs.remove(high1)
            high2 = max(pairs)
            res = [card for card in sorted_by_value_decreasing if card.value == high1]
            res = res + [card for card in sorted_by_value_decreasing if card.value == high2]
            for card in sorted_by_value_decreasing:
                if card.value != high1 and card.value != high2:
                    res.append(card)
                    break
            return (HandStrength.TWO_PAIR, res)
        #Pair
        elif len(pairs) == 1:
            high = max(pairs)
            res = [card for card in sorted_by_value_decreasing if card.value == high]
            for card in sorted_by_value_decreasing:
                if card.value != high:
                    res.append(card)
                if len(res) == 5:
                    break
        #High Card
        return (HandStrength.HIGH_CARD ,sorted_by_value_decreasing[:5])