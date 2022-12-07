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
    # count of iterations
    iters = 0
    while not is_sorted(arr):
        random.shuffle(arr)
        iters += 1
    return iters


def test():
    # three tests per dataset since this is literally random
    # plot time complexity

    # temporary with just first dataset
    # turns out even the first data set is slow as hell
    # array = open("datasets/data100.txt").readlines()
    # array = [int(x) for x in array]

    # Even smaller auto test cases (size of 5 through 10)
    for i in range(5, 16):
        # Create random values in array
        array = [random.randrange(30) for j in range(i)]

        # time start
        time_start = perf_counter()

        # run sort
        iterations_needed = bogo(array)

        # time stop
        time_stop = perf_counter()

        # calc time
        time_elapsed = time_stop - time_start

        print("For array of size", len(array))
        print("Time elapsed:", time_elapsed, "seconds")
        print("Total iterations:", iterations_needed)
        print("\n", "-"*30, "\n", sep="")


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