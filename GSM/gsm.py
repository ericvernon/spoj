import sys

__author__ = 'Eric'


class GamePredictor:
    """A class to predict the probability of winning a game, given a static probability of winning each point.
    """

    def __init__(self, prob, length=4):
        if prob > 1 or prob < 0:
            raise Exception("Probability must be between 0 and 1")
        self.prob = prob

        self.cache = []
        for i in range(length + 1):
            row = []
            for j in range(length + 1):
                if i == length:
                    row.append(1)
                elif j == length:
                    row.append(0)
                else:
                    row.append(-1)
            self.cache.append(row)

        # probability of winning a game, starting from a deuce. equal to (x^2)/(x^2)+(x-1)^2.
        deuce_seed = (prob ** 2) / ((2 * prob ** 2) - (2 * prob) + 1)
        self.cache[length - 1][length - 1] = deuce_seed

    def probability_winning(self, won=0, lost=0):
        """Find the probability of winning
        Keyword arguments:
        won -- how many points you have won
        lost -- how many points you have lost
        """
        p = self.cache[won][lost]
        if p != -1:
            return p

        p = self.prob * self.probability_winning(won + 1, lost) + (1 - self.prob) * self.probability_winning(won,
                                                                                                             lost + 1)
        self.cache[won][lost] = p
        return p


for line in sys.stdin:
    p = float(line)

    if p == -1:
        break

    # standard game, first to 4 points, win by two
    game = GamePredictor(p, 4)

    # set tiebreaker game, first to 7 points, win by two
    tiebreak = GamePredictor(p, 7)

    # the set predictor needs some special seeding to handle its win condition
    sets = GamePredictor(game.probability_winning(), 7)
    sets.cache[6][0] = sets.cache[6][1] = sets.cache[6][2] = sets.cache[6][3] = sets.cache[6][4] = 1
    sets.cache[0][6] = sets.cache[1][6] = sets.cache[2][6] = sets.cache[3][6] = sets.cache[4][6] = 0
    sets.cache[6][6] = tiebreak.probability_winning()

    # there are no special tie breaking rules for the match
    match = GamePredictor(sets.probability_winning(), 2)
    match.cache[1][1] = sets.probability_winning()

    print("{0:.11f} {1:.11f} {2:.11f}".format(game.probability_winning(), sets.probability_winning(),
                                              match.probability_winning()))
