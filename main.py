"""
To answer Terri's interview question(24 judegment poker game), I write the
answer as the following. Feel free to test.

This is the entrance of the program.
"""
from game_24 import Judge24


def main():
    solution = Judge24()
    cards = [4, 1, 8, 7]
    result = solution.judge24(cards)
    # # (8-4) * (7-1) = 24
    # print("It is ", result, " that you can get 24 with cards ", cards)

    # cards2 = [1, 2, 7, 13]
    # result2 = solution.judge24(cards2)
    # print("It is ", result2, " that you can get 24 with cards ", cards2)

    # cards3 = [3, 5, 20, 4]
    # result3 = solution.judge24(cards3)
    # # 3 + 5 + 20 - 4 = 24
    # print("It is ", result3, " that you can get 24 with cards ", cards3)

    # Do some experiments from [1,1,1,1] to [13,13,13,13]. What's the
    # probability that the problme is solvable.
    TOTAL_COMBINATION = 270725
    deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
            1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
            1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
            1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    countNumber = 0
    listOfCards = []
    for i in range(len(deck)):
        for j in range(i+1, len(deck)):
            for k in range(j+1, len(deck)):
                for x in range(k+1, len(deck)):
                    cards = [deck[i], deck[j], deck[k], deck[x]]
                    listOfCards.append(cards)

    for i in range(len(listOfCards)):
        if(solution.judge24(listOfCards[i])):
            countNumber += 1
    print("Of " + str(TOTAL_COMBINATION) + ", there are " + str(countNumber) +
          " that are solvable." + " And the probability is " +
          str(float(countNumber)/TOTAL_COMBINATION))
    # 218265 Of 270725 are solvable. And the probability is 0.806.


if __name__ == "__main__":
    main()
