"""
Advent of Code Day 2

# Don't try to compile Levenshtein, just get it from
# https://www.lfd.uci.edu/~gohlke/pythonlibs/#python-levenshtein
"""
from Levenshtein import distance, editops


def day_two():
    with open("data/day2.data", "r") as inf:
        codes = inf.readlines()

    two_dupe = 0
    three_dupe = 0
    found_leven = False
    for code in codes:
        # Challenge 1
        has_two, has_three = get_dupes(code)
        two_dupe += int(has_two)
        three_dupe += int(has_three)

        # Challenge 2
        if not found_leven:
            dist = [distance(code, x) for x in codes]
            if 1 in dist:
                print("Challenge 2 - first code: {0}".format(code), end="")
                print(
                    "Challenge 2 - second code: {0}".format(codes[dist.index(1)]),
                    end="",
                )

                # the editops show us which index differs between the two strings
                print(
                    "Challenge 2: edit ops: {0}".format(
                        editops(code, codes[dist.index(1)])
                    )
                )
                found_leven = (
                    True
                )  # No need to continue computing after we found the answer
    print("Challenge 1 Checksum: {0}".format(two_dupe * three_dupe))


def get_dupes(code):
    two, three = False, False
    unique_letters = set(code)
    for letter in unique_letters:
        if code.count(letter) == 2:
            two = True
        if code.count(letter) == 3:
            three = True

    return two, three


if __name__ == "__main__":
    day_two()
