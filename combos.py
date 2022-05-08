#!/usr/bin/env python3

import pandas as pd
import numpy as np
from itertools import combinations

"""
Say you have a CSV file with a bunch of reciptes and the requirements they satisfied - what combination of two
recipes satisfies all requirements?

This program allows you to import such a file and print all such combinations!
"""

def main(filename, max_index=12):
    """
    :param filename: csv file containing recipte options
    :param max index: the number of rows we wish to extract
    :return: None
    """

    # tweak to your use case:
    # start and end column indexes of the requirements
    reqs_start = 3
    reqs_end = 8

    # load the data into a numpy array
    data = np.array(pd.read_csv(filename))

    # extract the requirements as a boolean array, and the names a string array1
    reqs = data[:max_index, 3:8]
    names = data[:max_index, 0]

    # find combinations of names and requirements to
    combos = np.array(list(combinations(reqs, 2)))
    name_combos = np.array(list(combinations(names, 2)))

    # find the combination indexes of each combination which when logical or'd together sums to the total number of requirements
    indexes = np.where(np.sum(np.logical_or(combos[:,0,:], combos[:,1,:]), axis=1) == (reqs_end - reqs_start))

    # print the results in a table format
    padding = 22
    print("| Dish 1".ljust(padding) + " | Dish 2")
    print("-" * (padding + 1) + "|" + "-" * (padding + 1))
    for combo in name_combos[indexes]:
        print(("| " + str(combo[0][:padding-2])).ljust(padding) + (" |" + combo[1][:padding-5]))


if __name__ == "__main__":
    main("ideas.csv", max_index=12)
