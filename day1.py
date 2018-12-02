import numpy as np


def day_one():
    """
    Day 1 of Advent Of Code
    :return: None
    """
    with open("data/day1.data", "r") as data:
        frequencies = data.readlines()
    frequencies = np.asarray(frequencies, np.int64)

    print("Challenge 1: {0}".format(frequencies.sum(axis=0)))

    # Challenge 2
    passed = set()
    cur = 0
    while True:  # Ensuring we loop through frequencies until we find a duplicate
        for x in frequencies:
            cur += x
            if cur in passed:
                print("Challenge 2: {0}".format(cur))
                return None
            else:
                passed.add(cur)


if __name__ == "__main__":
    day_one()
