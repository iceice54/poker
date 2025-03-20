import pytest
from src.card import Card, Suit
from src.hand import Hand, PlayerHand, CommunityCards
from src.evaluator import Evaluator, HandStrength


@pytest.fixture
def evaluator():
    return Evaluator()


test_cases = [
    {
        "name": "Royal Flush",
        "player_hand": Hand(2, [Card(14, Suit.CLUBS), Card(13, Suit.CLUBS)]),
        "community_cards": Hand(
            5,
            [
                Card(12, Suit.CLUBS),
                Card(11, Suit.CLUBS),
                Card(10, Suit.CLUBS),
                Card(9, Suit.CLUBS),
                Card(8, Suit.CLUBS),
            ],
        ),
        "expected_strength": HandStrength.ROYAL_FLUSH,
        "expected_cards": [
            Card(14, Suit.CLUBS),
            Card(13, Suit.CLUBS),
            Card(12, Suit.CLUBS),
            Card(11, Suit.CLUBS),
            Card(10, Suit.CLUBS),
        ],
    },
    {
        "name": "Straight Flush",
        "player_hand": Hand(2, [Card(13, Suit.CLUBS), Card(12, Suit.CLUBS)]),
        "community_cards": Hand(
            5,
            [
                Card(10, Suit.CLUBS),
                Card(11, Suit.CLUBS),
                Card(9, Suit.CLUBS),
                Card(8, Suit.CLUBS),
                Card(7, Suit.CLUBS),
            ],
        ),
        "expected_strength": HandStrength.STRAIGHT_FLUSH,
        "expected_cards": [
            Card(13, Suit.CLUBS),
            Card(12, Suit.CLUBS),
            Card(11, Suit.CLUBS),
            Card(10, Suit.CLUBS),
            Card(9, Suit.CLUBS),
        ],
    },
    {
        "name": "Four of a Kind - highest",
        "player_hand": Hand(2, [Card(9, Suit.CLUBS), Card(9, Suit.HEARTS)]),
        "community_cards": Hand(
            5,
            [
                Card(9, Suit.SPADES),
                Card(9, Suit.DIAMONDS),
                Card(8, Suit.CLUBS),
                Card(7, Suit.CLUBS),
                Card(6, Suit.CLUBS),
            ],
        ),
        "expected_strength": HandStrength.FOUR_OF_A_KIND,
        "expected_cards": [
            Card(9, Suit.CLUBS),
            Card(9, Suit.HEARTS),
            Card(9, Suit.SPADES),
            Card(9, Suit.DIAMONDS),
            Card(8, Suit.CLUBS),
        ],
    },
    {
        "name": "Four of a Kind - middle",
        "player_hand": Hand(2, [Card(9, Suit.CLUBS), Card(9, Suit.HEARTS)]),
        "community_cards": Hand(
            5,
            [
                Card(9, Suit.SPADES),
                Card(9, Suit.DIAMONDS),
                Card(10, Suit.CLUBS),
                Card(11, Suit.CLUBS),
                Card(12, Suit.CLUBS),
            ],
        ),
        "expected_strength": HandStrength.FOUR_OF_A_KIND,
        "expected_cards": [
            Card(9, Suit.CLUBS),
            Card(9, Suit.HEARTS),
            Card(9, Suit.SPADES),
            Card(9, Suit.DIAMONDS),
            Card(12, Suit.CLUBS),
        ],
    },
    {
        "name": "Full House - 1 trip",
        "player_hand": Hand(2, [Card(10, Suit.CLUBS), Card(10, Suit.DIAMONDS)]),
        "community_cards": Hand(
            5,
            [
                Card(10, Suit.HEARTS),
                Card(9, Suit.HEARTS),
                Card(9, Suit.CLUBS),
                Card(7, Suit.HEARTS),
                Card(7, Suit.DIAMONDS),
            ],
        ),
        "expected_strength": HandStrength.FULL_HOUSE,
        "expected_cards": [
            Card(10, Suit.CLUBS),
            Card(10, Suit.DIAMONDS),
            Card(10, Suit.HEARTS),
            Card(9, Suit.HEARTS),
            Card(9, Suit.CLUBS),
        ],
    },
    {
        "name": "Full House - 2 trips",
        "player_hand": Hand(2, [Card(5, Suit.HEARTS), Card(8, Suit.DIAMONDS)]),
        "community_cards": Hand(
            5,
            [
                Card(5, Suit.DIAMONDS),
                Card(8, Suit.HEARTS),
                Card(8, Suit.SPADES),
                Card(14, Suit.CLUBS),
                Card(5, Suit.HEARTS),
            ],
        ),
        "expected_strength": HandStrength.FULL_HOUSE,
        "expected_cards": [
            Card(8, Suit.DIAMONDS),
            Card(8, Suit.HEARTS),
            Card(8, Suit.SPADES),
            Card(5, Suit.HEARTS),
            Card(5, Suit.DIAMONDS),
        ],
    },
    {
        "name": "Flush Test",
        "player_hand": Hand(2, [Card(5, Suit.CLUBS), Card(4, Suit.DIAMONDS)]),
        "community_cards": Hand(
            5,
            [
                Card(10, Suit.HEARTS),
                Card(2, Suit.HEARTS),
                Card(4, Suit.HEARTS),
                Card(12, Suit.HEARTS),
                Card(11, Suit.HEARTS),
            ],
        ),
        "expected_strength": HandStrength.FLUSH,
        "expected_cards": [
            Card(12, Suit.HEARTS),
            Card(11, Suit.HEARTS),
            Card(10, Suit.HEARTS),
            Card(4, Suit.HEARTS),
            Card(2, Suit.HEARTS),
        ],
    },
    {
        "name": "Straight Test",
        "player_hand": Hand(2, [Card(4, Suit.HEARTS), Card(5, Suit.HEARTS)]),
        "community_cards": Hand(
            5,
            [
                Card(8, Suit.DIAMONDS),
                Card(10, Suit.HEARTS),
                Card(14, Suit.DIAMONDS),
                Card(6, Suit.CLUBS),
                Card(7, Suit.HEARTS),
            ],
        ),
        "expected_strength": HandStrength.STRAIGHT,
        "expected_cards": [
            Card(8, Suit.DIAMONDS),
            Card(7, Suit.HEARTS),
            Card(6, Suit.CLUBS),
            Card(5, Suit.HEARTS),
            Card(4, Suit.HEARTS),
        ],
    },
    {
        "name": "Three of a Kind",
        "player_hand": Hand(2, [Card(5, Suit.HEARTS), Card(8, Suit.DIAMONDS)]),
        "community_cards": Hand(
            5,
            [
                Card(5, Suit.DIAMONDS),
                Card(10, Suit.HEARTS),
                Card(14, Suit.DIAMONDS),
                Card(6, Suit.CLUBS),
                Card(5, Suit.HEARTS),
            ],
        ),
        "expected_strength": HandStrength.THREE_OF_A_KIND,
        "expected_cards": [
            Card(5, Suit.HEARTS),
            Card(5, Suit.DIAMONDS),
            Card(5, Suit.HEARTS),
            Card(14, Suit.DIAMONDS),
            Card(10, Suit.HEARTS),
        ],
    },
    {
        "name": "Two Pair",
        "player_hand": PlayerHand([Card(5, Suit.HEARTS), Card(8, Suit.DIAMONDS)]),
        "community_cards": CommunityCards(
            [
                Card(5, Suit.DIAMONDS),
                Card(14, Suit.DIAMONDS),
                Card(13, Suit.HEARTS),
                Card(13, Suit.CLUBS),
                Card(8, Suit.SPADES),
            ]
        ),
        "expected_strength": HandStrength.TWO_PAIR,
        "expected_cards": [
            Card(13, Suit.HEARTS),
            Card(13, Suit.CLUBS),
            Card(8, Suit.DIAMONDS),
            Card(8, Suit.SPADES),
            Card(14, Suit.DIAMONDS),
        ],
    },
    {
        "name": "Pair",
        "player_hand": PlayerHand([Card(5, Suit.HEARTS), Card(8, Suit.DIAMONDS)]),
        "community_cards": CommunityCards(
            [
                Card(5, Suit.DIAMONDS),
                Card(14, Suit.DIAMONDS),
                Card(10, Suit.HEARTS),
                Card(13, Suit.CLUBS),
                Card(9, Suit.SPADES),
            ]
        ),
        "expected_strength": HandStrength.PAIR,
        "expected_cards": [
            Card(5, Suit.HEARTS),
            Card(5, Suit.DIAMONDS),
            Card(14, Suit.DIAMONDS),
            Card(13, Suit.CLUBS),
            Card(10, Suit.HEARTS),
        ],
    },
    {
        "name": "High Card",
        "player_hand": PlayerHand([Card(5, Suit.HEARTS), Card(8, Suit.DIAMONDS)]),
        "community_cards": CommunityCards(
            [
                Card(3, Suit.DIAMONDS),
                Card(14, Suit.DIAMONDS),
                Card(10, Suit.HEARTS),
                Card(13, Suit.CLUBS),
                Card(9, Suit.SPADES),
            ]
        ),
        "expected_strength": HandStrength.HIGH_CARD,
        "expected_cards": [
            Card(14, Suit.DIAMONDS),
            Card(13, Suit.CLUBS),
            Card(10, Suit.HEARTS),
            Card(9, Suit.SPADES),
            Card(8, Suit.DIAMONDS),
        ],
    },
]


@pytest.mark.parametrize(
    "player_hand, community_cards, expected_strength, expected_cards",
    [
        pytest.param(
            test_case["player_hand"],
            test_case["community_cards"],
            test_case["expected_strength"],
            test_case["expected_cards"],
            id=test_case["name"],
        )
        for test_case in test_cases
    ],
)
def test_calc_hand_strength(
    evaluator, player_hand, community_cards, expected_strength, expected_cards
):
    res = evaluator.calc_hand_strength(player_hand, community_cards)
    assert res == (expected_strength, expected_cards)
