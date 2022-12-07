import matplotlib.pyplot as plt
import random
import os
from time import perf_counter

def is_sorted(arr):
    # Find time complexity for built-in sorted and manual sort checking
    if arr == sorted(arr):
        return True
    return False

def bogo(arr):
    # Find time complexity with both manual shuffling and random.shuffle
    while not is_sorted(arr):
        random.shuffle(arr)


def test():
    # three tests per dataset since this is literally random
    # plot time complexity

    # temporary with just first dataset
    array = open("datasets/data100.txt").readlines()
    array = [int(x) for x in array]
    array = [10, 4, 2, 5, 9, 3, 1, 7, 8, 6]

    # time start
    time_start = perf_counter()

    # run sort
    bogo(array)

    # time stop
    time_stop = perf_counter()

    # calc time
    time_elapsed = time_stop - time_start

    print("Time elapsed:", time_elapsed, "seconds")


    # remove this later
    return


    # for both folders
    for folder in ["datasets", "datasetsSORTED"]:
        print("These are in the " + folder + " folder:\n")
        # open each file
        for filename in os.listdir(folder):
            # open the file and extract values
            file = open(folder + "/" + filename)
            array = file.readlines()
            # convert strings to ints
            array = [int(x) for x in array]

test()