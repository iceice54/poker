from .round import Round
from .deck import Deck
from .evaluator import Evaluator

def main():
    round = Round()
    round.deal_cards()
    round.progress_round()
    round.progress_round()
    round.progress_round()
    evaluator = Evaluator()
    evaluator.calc_hand_strength(round.player1_hand, round.community_cards)