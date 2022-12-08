###############################################################################
# This program allows for the transfer from java outfile to matplotlib.pyplot #
###############################################################################

import matplotlib.pyplot as plt
import numpy as np

def graph(filename):
    # creating the pyplot graphs from a text file

    file = open(filename)

    # NOT THIS EASY :(
    # Data needs to equal the last line of file
    #data = eval(file.readlines()[-1])

    # New way of extracting data based on file formatting
    data = []
    lines = file.readlines()
    for i in range(len(lines)):
        if "For array of size:" in lines[i]:
            data.append( [ int(lines[i][19:]), eval(lines[i+1][10:-8]), int(lines[i+2][18:]) ] )
        
    file.close()


    plt.rcParams['axes.autolimit_mode'] = 'round_numbers'

    f, (ax1, ax2) = plt.subplots(1, 2, sharex=True, figsize=(10, 5)) 

    f.suptitle("Bogosort Efficiency by Time and Iterations")

    # Plotting time
    ax1.plot(
        [ x[0] for x in data ], # x-axis
        [ y[1] for y in data ], # y-axis
        "-x"
    )

    ax1.set_title('Time in Seconds')
    ax1.set_xlabel("Array Size")
    ax1.set_xlim(data[0][0], data[-1][0])
    ax1.set_ylim(0, data[-1][1])
    ax1.set_box_aspect(1)


    # Plotting iterations
    ax2.plot(
        [ x[0] for x in data ], # x-axis
        [ y[2] for y in data ], # y-axis
        "-x"
    )

    ax2.set_title('Iterations')
    ax2.set_xlabel("Array Size")
    # only have to do this once b/c sharex is True
    ax2.set_xticks(np.arange(data[0][0], data[-1][0] + 1, 1))
    #ax2.set_yticks(np.arange(data[0][2], data[-1][2] + 1))
    ax2.set_xlim(data[0][0], data[-1][0])
    ax2.set_ylim(0, data[-1][2] + 1)
    ax2.set_box_aspect(1)

    plt.subplots_adjust(
        wspace=0.5
    )

    #plt.savefig('5_20_results.png')
    plt.show()


graph("results_java.txt")