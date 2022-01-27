# we create this class to prevent the repetition of dice in the different functions
class Hand:
    def __init__(self, d1, d2, d3, d4, d5):
        self.dice = [0] * 5
        self.dice[0] = d1
        self.dice[1] = d2
        self.dice[2] = d3
        self.dice[3] = d4
        self.dice[4] = d5


"""this function will be used in scoring functions section. We define it so that we can reuse it and remove 
redundancy from scoring computing"""
def score(hand, number):
    sum = 0
    for die in hand.dice:
        if die == number:
            sum += die
    return sum


# this function will be used in three of a kind and four of a kind section. Its purpose is to remove redundancy
def number_of_a_kind(hand, number):
    # Initialisation of all dice values to 0 in a dictionary
    counts = dict.fromkeys(range(1, 7), 0)

    # counting the occurrence of each dice
    for value in hand.dice:
        counts[value] = counts[value] + 1

    for key in reversed(range(1, 7)):
        if counts[key] >= number:
            return key * number
    return 0


class Yatzy:

    @staticmethod
    def chance(d1, d2, d3, d4, d5):
        return d1 + d2 + d3 + d4 + d5

    @staticmethod
    def yatzy(dice):
        # Checking if all the element are similar to the first element of the list. if yes return 50 otherwise
        # return 0, we can also use count function by comparing the occurrences of the first element to len of list
        if all(element == dice[0] for element in dice):
            return 50
        else:
            return 0

    @staticmethod
    def ones(hand):
        # We used the score function defined at the beginning
        return score(hand, 1)

    @staticmethod
    def twos(hand):
        # We reused the score function defined at the beginning
        return score(hand, 2)

    @staticmethod
    def threes(hand):
        # We reused the score function defined at the beginning
        return score(hand, 3)

    @staticmethod
    def fours(hand):
        # We reused the score function defined at the beginning
        return score(hand, 4)

    @staticmethod
    def fives(hand):
        # We reused the score function defined at the beginning
        return score(hand, 5)

    @staticmethod
    def sixes(hand):
        # We reused the score function defined at the beginning
        return score(hand, 6)

    @staticmethod
    def one_pair(hand):
        # Initialisation of all dice values to 0 in a dictionary
        counts = dict.fromkeys(range(1, 7), 0)

        # counting the occurrence of each dice
        for value in hand.dice:
            counts[value] = counts[value] + 1

        for key in reversed(range(1, 7)):
            if counts[key] >= 2:
                return key * 2
        return 0

    @staticmethod
    def two_pairs(hand):
        counts = dict.fromkeys(range(1, 7), 0)
        for value in hand.dice:
            counts[value] = counts[value] + 1

        # variable to check weather the number of pairs is equal to 1 or 2
        number_of_pairs = 0

        # variable to stock the score
        sum_of_scores = 0
        for key in reversed(range(1, 7)):
            if counts[key] >= 2:
                number_of_pairs += 1
                sum_of_scores += key * 2
        if number_of_pairs == 2:
            return sum_of_scores
        return 0

    @staticmethod
    def three_of_a_kind(hand):
        return number_of_a_kind(hand, 3)

    @staticmethod
    def four_of_a_kind(hand):
        return number_of_a_kind(hand, 4)

    @staticmethod
    # The purpose of small straight is to check if the elements of the dice are 1, 2, 3, 4, 5 if no we return 0
    # otherwise we return 15, so we can use sort method in order to compare the dice list to [1, 2, 3, 4, 5]
    def small_straight(hand):
        hand.dice.sort()
        if hand.dice != [1, 2, 3, 4, 5]:
            return 0
        return 15

    @staticmethod
    # We apply the same thing as we did in small straight
    def large_straight(hand):
        hand.dice.sort()
        if hand.dice != [2, 3, 4, 5, 6]:
            return 0
        return 20

    @staticmethod
    def full_house(hand):
        two_of_a_kind_score = number_of_a_kind(hand, 2)
        three_of_a_kind_score = number_of_a_kind(hand, 3)
        if (two_of_a_kind_score != 0) and (three_of_a_kind_score != 0):
            return two_of_a_kind_score + three_of_a_kind_score
        return 0
