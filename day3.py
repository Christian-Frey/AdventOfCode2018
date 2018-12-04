"""Day 3 of Advent of Code"""
import re
from dataclasses import dataclass

import numpy as np


@dataclass()
class Claim:
    def __init__(self, idx, start_x, start_y, dim_x, dim_y):
        self.idx = int(idx)
        self.start_x = int(start_x)
        self.start_y = int(start_y)
        self.dim_x = int(dim_x)
        self.dim_y = int(dim_y)

        self.end_x = self.dim_x + self.start_x
        self.end_y = self.start_y + self.dim_y
        self.grid_coverage = np.ones((self.dim_x, self.dim_y))


def day_03():
    with open("data/day_03.data", "r") as inf:
        lines = inf.readlines()

    num_find = re.compile("\d+")
    claims = []
    for c in lines:
        claim_split = num_find.findall(c)
        claims.append(Claim(*claim_split))

    full_cloth = np.zeros((2000, 2000))
    for c in claims:
        # Define a window in the numpy array. Then add that window to the ones
        # array we created earlier, so we slowly add up the squares.
        full_cloth[c.start_x : c.end_x, c.start_y : c.end_y] = (
            full_cloth[c.start_x : c.end_x, c.start_y : c.end_y] + c.grid_coverage
        )
    # Count where each cell in full_cloth <= 2
    overlap = np.count_nonzero(2 <= full_cloth)
    print("Challenge 1: {0}".format(overlap))

    # Double loop... Numpy makes it fast enough
    for c in claims:
        # Get the subarray, and find the subarray which has a max value of 1
        if np.amax(full_cloth[c.start_x : c.end_x, c.start_y : c.end_y]) == 1:
            print("Challenge 2: #{0}".format(c.idx))


if __name__ == "__main__":
    day_03()
