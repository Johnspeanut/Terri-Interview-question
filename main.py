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
    # (8-4) * (7-1) = 24
    print("It is ", result, " that you can get 24 with cards ", cards)

    cards2 = [1, 2, 7, 13]
    result2 = solution.judge24(cards2)
    print("It is ", result2, " that you can get 24 with cards ", cards2)

    cards3 = [3, 5, 20, 4]
    result3 = solution.judge24(cards3)
    # 3 + 5 + 20 - 4 = 24
    print("It is ", result3, " that you can get 24 with cards ", cards3)


if __name__ == "__main__":
    main()
