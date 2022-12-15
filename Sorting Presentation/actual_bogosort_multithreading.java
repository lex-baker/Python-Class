import java.util.*;
import java.io.File;  // Import the File class
import java.io.IOException;
import java.io.FileWriter;

class actual_bogosort_multithreading {
    public static void main(String[] args) {
        try {

            File file = new File("15_20_results_java.txt");
            if (file.createNewFile()) {
                System.out.println("File created: " + file.getName() + "\n");
            } else {
                System.out.println("File already exists.");
                System.exit(0);
            }
            
            for(int i = 15; i < 21; i++) {
                test(i, file);
            }
            


        } catch (IOException e) {
            System.out.println("An error occurred.");
        }

        
    }


    public static void test(int size, File outfile) {
        try {
            FileWriter fr = new FileWriter(outfile, true);

            ArrayList<Integer> array = create_random_array(size);

            // Start timer
            long startTime = System.nanoTime();

            // Run the bogosort
            int iterations = bogosort(array);
            
            // End timer
            long endTime = System.nanoTime();

            float timeElapsed = (float) (endTime - startTime) / (float) 1e+9;

            //System.out.println("That took " + (endTime - startTime) + " nanoseconds");
            System.out.println("For array of size: " + array.size());
            System.out.println("That took " + timeElapsed + " seconds");
            System.out.println("Total iterations: " + iterations);
            System.out.println("\n------------------------------\n\n");

            fr.write("For array of size: " + array.size() + "\n");
            fr.write("That took " + timeElapsed + " seconds\n");
            fr.write("Total iterations: " + iterations + "\n");
            fr.write("\n------------------------------\n\n");

            fr.close();
        } catch (IOException e) {
            System.out.println(e);
        }

    }

    public static ArrayList<Integer> create_random_array(int size) {
        ArrayList<Integer> array = new ArrayList<Integer>();
        for(int i = 0; i < size; i++) {
            array.add(i);
        }
        Collections.shuffle(array);
        return array;
    }

    public static int bogosort(ArrayList<Integer> array) {
        int iters = 0;
        while(is_sorted(array) == false) {
            Collections.shuffle(array);
            iters += 1;
        }
        return iters;
    }

    public static boolean is_sorted(ArrayList<Integer> arr) {
        for (int i = 1; i < arr.size(); i++)
    
            // Unsorted pair found
            if (arr.get(i - 1) > arr.get(i))
                return false;
    
        // No unsorted pair found
        return true;
    }
}






/*
import matplotlib.pyplot as plt
import random
import os
from time import perf_counter
import numpy as np

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

    outfile = open('5_20_results.txt', 'w')

    data = []

    # Even smaller auto test cases (size of 5 through 10)
    for i in range(5, 21):
        # Create iterative values in array and randomize
        array = [j for j in range(i)]
        random.shuffle(array)

        # time start
        time_start = perf_counter()

        # run sort
        iterations_needed = bogo(array)

        # time stop
        time_stop = perf_counter()

        # calc time
        time_elapsed = time_stop - time_start

        # Print to terminal
        print("For array of size:", len(array))
        print("Time elapsed:", time_elapsed, "seconds")
        print("Total iterations:", iterations_needed)
        print("\n", "-"*30, "\n", sep="")

        # Print to outfile
        print("For array of size:", len(array), file=outfile)
        print("Time elapsed:", time_elapsed, "seconds", file=outfile)
        print("Total iterations:", iterations_needed, file=outfile)
        print("\n", "-"*30, "\n", sep="", file=outfile)

        data.append( [len(array), time_elapsed, iterations_needed] )

    print(data)
    print(data, file=outfile)

    outfile.close()

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

    plt.savefig('5_20_results.png')
    plt.show()

    


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
*/