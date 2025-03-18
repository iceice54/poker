from .hand import PlayerHand, CommunityCards
from .deck import Deck

class Round():
    def __init__(self) -> None:
        self.deck = Deck()
        self.community_cards = CommunityCards()
        self.player1_hand = PlayerHand()
        self.player2_hand = PlayerHand()
        self.player_hands: list[PlayerHand] = [self.player1_hand, self.player2_hand]

    def deal_cards(self) -> None:
        for hand in self.player_hands:
            for _ in range(2):
                hand.add_card(self.deck.deal_card())
        print("Player 1's hand is " + str(self.player1_hand))
        print("Player 2's hand is " + str(self.player2_hand))

    def progress_round(self) -> None:
        if len(self.community_cards) >= 5:
            raise ValueError("All community cards have already been dealt!")
        if len(self.community_cards) == 0:
            for _ in range(3):
                self.community_cards.add_card(self.deck.deal_card())
            print("Flop!")
        elif len(self.community_cards) == 3:
            self.community_cards.add_card(self.deck.deal_card())
            print("Turn!")
        elif len(self.community_cards) == 4:
            self.community_cards.add_card(self.deck.deal_card())
            print("River!")
        print("Community cards are " + str(self.community_cards))
        