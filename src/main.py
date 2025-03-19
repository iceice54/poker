from .round import Round
from .deck import Deck
from .evaluator import Evaluator
from .card import Card, Suit

def main():
    # round = Round()
    # round.deal_cards()
    # round.progress_round()
    # round.progress_round()
    # round.progress_round()
    # evaluator = Evaluator()
    # evaluator.calc_hand_strength(round.player1_hand, round.community_cards)
    community_cards = [Card(3, Suit.DIAMONDS), Card(11, Suit.CLUBS), Card(5, Suit.CLUBS), Card(7, Suit.CLUBS), Card(13, Suit.CLUBS)]
    print([card.value for card in sorted(community_cards, reverse=True)])
