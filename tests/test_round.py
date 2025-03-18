import pytest
from src.round import Round

def test_deal_cards() -> None:
    round = Round()
    round.deal_cards()
    assert len(round.player1_hand)==2
    assert len(round.player2_hand)==2

def test_exceed_community_cards() -> None:
    round = Round()
    for _ in range(3):
        round.progress_round()
    with pytest.raises(ValueError):
        round.progress_round()