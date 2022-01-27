from yatzy import Yatzy
from yatzy import Hand


# These unit tests can be run using the py.test framework
# available from http://pytest.org/

def test_chance():
    assert 15 == Yatzy.chance(2, 3, 4, 5, 1)
    assert 16 == Yatzy.chance(3, 3, 4, 5, 1)


def test_yatzy():
    expected = 50
    assert expected == Yatzy.yatzy([4, 4, 4, 4, 4])
    assert expected == Yatzy.yatzy([6, 6, 6, 6, 6])
    assert 0 == Yatzy.yatzy([6, 6, 6, 6, 3])


def test_ones():
    assert 0 == Yatzy.ones(Hand(6, 2, 2, 4, 5))
    assert 1 == Yatzy.ones(Hand(1, 2, 3, 4, 5))
    assert 2 == Yatzy.ones(Hand(1, 2, 1, 4, 5))
    assert 4 == Yatzy.ones(Hand(1, 2, 1, 1, 1))


def test_twos():
    assert 4 == Yatzy.twos(Hand(1, 2, 3, 2, 6))
    assert 10 == Yatzy.twos(Hand(2, 2, 2, 2, 2))


def test_threes():
    assert 6 == Yatzy.threes(Hand(1, 2, 3, 2, 3))
    assert 12 == Yatzy.threes(Hand(2, 3, 3, 3, 3))


def test_fours():
    assert 4 == Yatzy.fours(Hand(4, 5, 5, 5, 5))
    assert 8 == Yatzy.fours(Hand(4, 4, 5, 5, 5))
    assert 12 == Yatzy.fours(Hand(4, 4, 4, 5, 5))


def test_fives():
    assert 10 == Yatzy.fives(Hand(4, 4, 4, 5, 5))
    assert 20 == Yatzy.fives(Hand(4, 5, 5, 5, 5))
    assert 15 == Yatzy.fives(Hand(4, 4, 5, 5, 5))


def test_sixes():
    assert 0 == Yatzy.sixes(Hand(4, 4, 4, 5, 5))
    assert 6 == Yatzy.sixes(Hand(4, 4, 6, 5, 5))
    assert 18 == Yatzy.sixes(Hand(6, 5, 6, 6, 5))


def test_one_pair():
    assert 6 == Yatzy.one_pair(Hand(3, 4, 3, 5, 6))
    assert 10 == Yatzy.one_pair(Hand(5, 3, 3, 3, 5))
    assert 12 == Yatzy.one_pair(Hand(5, 3, 6, 6, 5))


def test_two_pairs():
    assert 16 == Yatzy.two_pairs(Hand(3, 3, 5, 4, 5))
    assert 18 == Yatzy.two_pairs(Hand(3, 3, 6, 6, 6))
    assert 0 == Yatzy.two_pairs(Hand(3, 3, 6, 5, 4))


def test_three_of_a_kind():
    assert 9 == Yatzy.three_of_a_kind(Hand(3, 3, 3, 4, 5))
    assert 9 == Yatzy.three_of_a_kind(Hand(3, 3, 3, 3, 5))
    assert 15 == Yatzy.three_of_a_kind(Hand(5, 3, 5, 4, 5))



def test_four_of_a_kind():
    assert 12 == Yatzy.four_of_a_kind(Hand(3, 3, 3, 3, 5))
    assert 12 == Yatzy.four_of_a_kind(Hand(3, 3, 3, 3, 3))
    assert 20 == Yatzy.four_of_a_kind(Hand(5, 5, 5, 4, 5))
    assert 0 == Yatzy.four_of_a_kind(Hand(3, 3, 3, 2, 1))


def test_small_straight():
    assert 15 == Yatzy.small_straight(Hand(1, 2, 3, 4, 5))
    assert 15 == Yatzy.small_straight(Hand(2, 3, 4, 5, 1))
    assert 0 == Yatzy.small_straight(Hand(1, 2, 2, 4, 5))


def test_large_straight():
    assert 20 == Yatzy.large_straight(Hand(6, 2, 3, 4, 5))
    assert 20 == Yatzy.large_straight(Hand(2, 3, 4, 5, 6))
    assert 0 == Yatzy.large_straight(Hand(1, 2, 2, 4, 5))


def test_full_house():
    assert 18 == Yatzy.full_house(Hand(6, 2, 2, 2, 6))
    assert 0 == Yatzy.full_house(Hand(2, 3, 4, 5, 6))
