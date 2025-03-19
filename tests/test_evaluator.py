import pytest
from src.card import Card, Suit
from src.hand import Hand
from src.evaluator import Evaluator, HandStrength

@pytest.fixture
def evaluator():
    return Evaluator()

royal_flush_cases = [
    {
        "name": "Royal Flush - Clubs",
        "player_hand": Hand(2, [Card(14, Suit.CLUBS), Card(13, Suit.CLUBS)]),
        "community_cards": Hand(5, [
            Card(12, Suit.CLUBS), Card(11, Suit.CLUBS), Card(10, Suit.CLUBS),
            Card(9, Suit.CLUBS), Card(8, Suit.CLUBS)
        ]),
        "expected_strength": HandStrength.ROYAL_FLUSH,
        "expected_cards": [
            Card(14, Suit.CLUBS), Card(13, Suit.CLUBS), Card(12, Suit.CLUBS),
            Card(11, Suit.CLUBS), Card(10, Suit.CLUBS)
        ]
    }
]

@pytest.mark.parametrize(
        "player_hand, community_cards, expected_strength, expected_cards", 
        [
            pytest.param(
                test_case["player_hand"], test_case["community_cards"],
                test_case["expected_strength"], test_case["expected_cards"],
                id=test_case["name"]
            )
            for test_case in royal_flush_cases
        ]
)

def test_royal_flush(evaluator, player_hand, community_cards, expected_strength, expected_cards):
    res = evaluator.calc_hand_strength(player_hand, community_cards)
    assert res == (expected_strength, expected_cards)


# test_cases = [
#         # Royal Flush Test Case
#         (Hand(2, [Card(14, Suit.CLUBS), Card(13, Suit.CLUBS)]), 
#          Hand(5, [Card(12, Suit.CLUBS), Card(11, Suit.CLUBS), Card(10, Suit.CLUBS), 
#                   Card(9, Suit.CLUBS), Card(8, Suit.CLUBS)]), 
#          HandStrength.ROYAL_FLUSH, 
#          [Card(14, Suit.CLUBS), Card(13, Suit.CLUBS), Card(12, Suit.CLUBS), 
#           Card(11, Suit.CLUBS), Card(10, Suit.CLUBS)]),
        
#         # Straight Flush Test Case
#         (Hand(2, [Card(13, Suit.CLUBS), Card(12, Suit.CLUBS)]), 
#          Hand(5, [Card(10, Suit.CLUBS), Card(11, Suit.CLUBS), Card(9, Suit.CLUBS), 
#                   Card(8, Suit.CLUBS), Card(7, Suit.CLUBS)]), 
#          HandStrength.STRAIGHT_FLUSH, 
#          [Card(13, Suit.CLUBS), Card(12, Suit.CLUBS), Card(11, Suit.CLUBS), 
#           Card(10, Suit.CLUBS), Card(9, Suit.CLUBS)]),
        
#         # Four of a Kind Test Case
#         (Hand(2, [Card(9, Suit.CLUBS), Card(9, Suit.HEARTS)]), 
#          Hand(5, [Card(9, Suit.SPADES), Card(9, Suit.DIAMONDS), Card(10, Suit.CLUBS), 
#                   Card(11, Suit.CLUBS), Card(12, Suit.CLUBS)]), 
#          HandStrength.FOUR_OF_A_KIND, 
#          [Card(9, Suit.CLUBS), Card(9, Suit.HEARTS), Card(9, Suit.SPADES), 
#           Card(9, Suit.DIAMONDS), Card(12, Suit.CLUBS)]),
        
#         # Full House Test Case
#         (Hand(2, [Card(10, Suit.CLUBS), Card(10, Suit.DIAMONDS)]), 
#          Hand(5, [Card(10, Suit.HEARTS), Card(9, Suit.HEARTS), Card(9, Suit.CLUBS), 
#                   Card(7, Suit.HEARTS), Card(7, Suit.DIAMONDS)]), 
#          HandStrength.FULL_HOUSE, 
#          [Card(10, Suit.CLUBS), Card(10, Suit.DIAMONDS), Card(10, Suit.HEARTS), 
#           Card(9, Suit.HEARTS), Card(9, Suit.CLUBS)]),
        
#         # Flush Test Case
#         (Hand(2, [Card(5, Suit.CLUBS), Card(4, Suit.DIAMONDS)]), 
#          Hand(5, [Card(10, Suit.HEARTS), Card(2, Suit.HEARTS), Card(4, Suit.HEARTS), 
#                   Card(12, Suit.HEARTS), Card(11, Suit.HEARTS)]), 
#          HandStrength.FLUSH, 
#          [Card(12, Suit.HEARTS), Card(11, Suit.HEARTS), Card(10, Suit.HEARTS), 
#           Card(4, Suit.HEARTS), Card(2, Suit.HEARTS)]),
        
#         # Straight Test Case
#         (Hand(2, [Card(4, Suit.HEARTS), Card(5, Suit.HEARTS)]), 
#          Hand(5, [Card(8, Suit.DIAMONDS), Card(10, Suit.HEARTS), Card(14, Suit.DIAMONDS), 
#                   Card(6, Suit.CLUBS), Card(7, Suit.HEARTS)]), 
#          HandStrength.STRAIGHT, 
#          [Card(8, Suit.DIAMONDS), Card(7, Suit.HEARTS), Card(6, Suit.CLUBS), 
#           Card(5, Suit.HEARTS), Card(4, Suit.HEARTS)]),
        
#         # Three of a Kind Test Case
#         (Hand(2, [Card(5, Suit.HEARTS), Card(8, Suit.DIAMONDS)]), 
#          Hand(5, [Card(5, Suit.DIAMONDS), Card(10, Suit.HEARTS), Card(14, Suit.DIAMONDS), 
#                   Card(6, Suit.CLUBS), Card(5, Suit.HEARTS)]), 
#          HandStrength.THREE_OF_A_KIND, 
#          [Card(5, Suit.HEARTS), Card(5, Suit.DIAMONDS), Card(5, Suit.HEARTS), 
#           Card(14, Suit.DIAMONDS), Card(10, Suit.HEARTS)]),
#     ]

# def test_check_flush() -> None:
#     evaluator = Evaluator()
#     player_hand = Hand(2, [Card(14, Suit.CLUBS), Card(12, Suit.CLUBS)])
#     community_cards = Hand(5, [Card(13, Suit.CLUBS), Card(11, Suit.CLUBS), Card(10, Suit.CLUBS), Card(9, Suit.CLUBS), Card(8, Suit.CLUBS)])
#     sorted_by_value_decreasing = sorted(player_hand.cards + community_cards.cards, reverse=True)
#     res = evaluator.check_flush(sorted_by_value_decreasing)
#     assert res == [Card(14, Suit.CLUBS), Card(13, Suit.CLUBS), Card(12, Suit.CLUBS), Card(11, Suit.CLUBS), Card(10, Suit.CLUBS), Card(9, Suit.CLUBS), Card(8, Suit.CLUBS)]

#     player_hand = Hand(2, [Card(14, Suit.CLUBS), Card(13, Suit.CLUBS)])
#     community_cards = Hand(5, [Card(12, Suit.CLUBS), Card(11, Suit.CLUBS), Card(10, Suit.DIAMONDS), Card(9, Suit.HEARTS), Card(8, Suit.SPADES)])
#     sorted_by_value_decreasing = sorted(player_hand.cards + community_cards.cards, reverse=True)
#     res = evaluator.check_flush(sorted_by_value_decreasing)
#     assert res == None

# def test_check_straight() -> None:
#     evaluator = Evaluator()
#     player_hand = Hand(2, [Card(14, Suit.DIAMONDS), Card(13, Suit.CLUBS)])
#     community_cards = Hand(5, [Card(12, Suit.HEARTS), Card(11, Suit.CLUBS), Card(10, Suit.HEARTS), Card(9, Suit.CLUBS), Card(8, Suit.CLUBS)])
#     res = evaluator.check_straight(player_hand.cards + community_cards.cards)
#     assert res == [Card(14, Suit.DIAMONDS), Card(13, Suit.CLUBS), Card(12, Suit.HEARTS), Card(11, Suit.CLUBS), Card(10, Suit.HEARTS)]

#     player_hand = Hand(2, [Card(14, Suit.CLUBS), Card(13, Suit.CLUBS)])
#     community_cards = Hand(5, [Card(12, Suit.CLUBS), Card(10, Suit.CLUBS), Card(9, Suit.DIAMONDS), Card(8, Suit.HEARTS), Card(7, Suit.SPADES)])
#     res = evaluator.check_straight(player_hand.cards + community_cards.cards)
#     assert res == None

# def test_royal_flush() -> None:
#     evaluator = Evaluator()
#     player_hand = Hand(2, [Card(14, Suit.CLUBS), Card(13, Suit.CLUBS)])
#     community_cards = Hand(5, [Card(12, Suit.CLUBS), Card(11, Suit.CLUBS), Card(10, Suit.CLUBS), Card(9, Suit.CLUBS), Card(8, Suit.CLUBS)])
#     res = evaluator.calc_hand_strength(player_hand, community_cards)
#     assert res == (HandStrength.ROYAL_FLUSH, [Card(14, Suit.CLUBS), Card(13, Suit.CLUBS), Card(12, Suit.CLUBS), Card(11, Suit.CLUBS), Card(10, Suit.CLUBS)])

# def test_straight_flush() -> None:
#     evaluator = Evaluator()
#     player_hand = Hand(2, [Card(13, Suit.CLUBS), Card(12, Suit.CLUBS)])
#     community_cards = Hand(5, [Card(10, Suit.CLUBS), Card(11, Suit.CLUBS), Card(9, Suit.CLUBS), Card(8, Suit.CLUBS), Card(7, Suit.CLUBS)])
#     res = evaluator.calc_hand_strength(player_hand, community_cards)
#     assert res == (HandStrength.STRAIGHT_FLUSH, [Card(13, Suit.CLUBS), Card(12, Suit.CLUBS), Card(11, Suit.CLUBS), Card(10, Suit.CLUBS), Card(9, Suit.CLUBS)])

# def test_four_of_a_kind() -> None:
#     evaluator = Evaluator()
#     player_hand = Hand(2, [Card(9, Suit.CLUBS), Card(9, Suit.HEARTS)])
#     community_cards = Hand(5, [Card(9, Suit.SPADES), Card(9, Suit.DIAMONDS), Card(10, Suit.CLUBS), Card(11, Suit.CLUBS), Card(12, Suit.CLUBS)])
#     res = evaluator.calc_hand_strength(player_hand, community_cards)
#     assert res == (HandStrength.FOUR_OF_A_KIND, [Card(9, Suit.CLUBS), Card(9, Suit.HEARTS), Card(9, Suit.SPADES), Card(9, Suit.DIAMONDS), Card(12, Suit.CLUBS)])

# def test_full_house() -> None:
#     evaluator = Evaluator()
#     player_hand = Hand(2, [Card(10, Suit.CLUBS), Card(10, Suit.DIAMONDS)])
#     community_cards = Hand(5, [Card(10, Suit.HEARTS), Card(9, Suit.HEARTS), Card(9, Suit.CLUBS), Card(7, Suit.HEARTS), Card(7, Suit.DIAMONDS)])
#     res = evaluator.calc_hand_strength(player_hand, community_cards)
#     assert res == (HandStrength.FULL_HOUSE, [Card(10, Suit.CLUBS), Card(10, Suit.DIAMONDS), Card(10, Suit.HEARTS), Card(9, Suit.HEARTS), Card(9, Suit.CLUBS)])

#     player_hand = Hand(2, [Card(9, Suit.CLUBS), Card(9, Suit.DIAMONDS)])
#     community_cards = Hand(5, [Card(10, Suit.CLUBS), Card(10, Suit.DIAMONDS), Card(8, Suit.DIAMONDS), Card(8, Suit.HEARTS), Card(10, Suit.SPADES)])
#     res = evaluator.calc_hand_strength(player_hand, community_cards)
#     assert res == (HandStrength.FULL_HOUSE, [Card(10, Suit.CLUBS), Card(10, Suit.DIAMONDS), Card(10, Suit.SPADES), Card(9, Suit.CLUBS), Card(9, Suit.DIAMONDS)])

# def test_flush() -> None:
#     evaluator = Evaluator()
#     player_hand = Hand(2, [Card(5, Suit.CLUBS), Card(4, Suit.DIAMONDS)])
#     community_cards = Hand(5, [Card(10, Suit.HEARTS), Card(2, Suit.HEARTS), Card(4, Suit.HEARTS), Card(12, Suit.HEARTS), Card(11, Suit.HEARTS)])
#     res = evaluator.calc_hand_strength(player_hand, community_cards)
#     assert res == (HandStrength.FLUSH, [Card(12, Suit.HEARTS), Card(11, Suit.HEARTS), Card(10, Suit.HEARTS), Card(4, Suit.HEARTS), Card(2, Suit.HEARTS)])

# def test_straight() -> None:
#     evaluator = Evaluator()
#     player_hand = Hand(2, [Card(4, Suit.HEARTS), Card(5, Suit.HEARTS)])
#     community_cards = Hand(5, [Card(8, Suit.DIAMONDS), Card(10, Suit.HEARTS), Card(14, Suit.DIAMONDS), Card(6, Suit.CLUBS), Card(7, Suit.HEARTS)])
#     res = evaluator.calc_hand_strength(player_hand, community_cards)
#     assert res == (HandStrength.STRAIGHT, [Card(8, Suit.DIAMONDS), Card(7, Suit.HEARTS), Card(6, Suit.CLUBS), Card(5, Suit.HEARTS), Card(4, Suit.HEARTS)])

# def test_three_of_a_kind() -> None:
#     evaluator = Evaluator()
#     player_hand = Hand(2, [Card(5, Suit.HEARTS), Card(8, Suit.DIAMONDS)])
#     community_cards = Hand(5, [Card(5, Suit.DIAMONDS), Card(10, Suit.HEARTS), Card(14, Suit.DIAMONDS), Card(6, Suit.CLUBS), Card(5, Suit.HEARTS)])
#     res = evaluator.calc_hand_strength(player_hand, community_cards)
#     assert res == (HandStrength.THREE_OF_A_KIND, [Card(5, Suit.HEARTS), Card(5, Suit.DIAMONDS), Card(5, Suit.HEARTS), Card(14, Suit.DIAMONDS), Card(10, Suit.HEARTS)])


