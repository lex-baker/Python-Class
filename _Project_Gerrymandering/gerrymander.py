#########################
# Author: Lex Baker
# Date: 10/31/22
# On my honor, I neither gave nor received unauthorized help on this project
#########################


# Import the graphics.py module
from graphics import *

"""
Main file which calls all other functions
"""
def main():
    # Set the constant variables
    WIDTH = 500
    HEIGHT = 500
    EGTHRESHOLD = .07

    # Check that the files exist and open them if so
    try:
        # Access the districts.txt file
        districts_file = open("districts.txt")
        all_states_districts = districts_file.readlines()
        districts_file.close()

        # Access the eligible_voters.txt file
        voters_file = open("eligible_voters.txt")
        all_states_voters = voters_file.readlines()
        voters_file.close()
    except FileNotFoundError:
        print("Cannot find one or more neccessary files")
        exit()

    # Explain what this program does
    print("This program allows you to search through data about congressional voting districts")
    print("and determine whether a particular state is gerrymandered.\n")
    # Have the user input a state
    input_state = input("Which state do you want to look up? ")
    print(input_state)
    # Attempt to get district info for given state
    raw_district_info = get_district_info(input_state, all_states_districts)
    # Only proceed if state was found in districts.txt
    if raw_district_info != None:
        # Save state name (for graphics window)
        state_name = raw_district_info[0]
        # Get the total number of voters
        total_voters = get_voter_info(input_state, all_states_voters)
        # Change the format of the array of districts and their respective tallies of votes
        district_info = filter_districts(raw_district_info)
        # Calculate wasted democratic and republican votes as an array of [wasted Democrat votes, wasted Republican votes]
        wasted_votes = find_waste(district_info)
        # Print information found thus far
        print("Total Wasted Democratic votes:", wasted_votes[0])
        print("Total Wasted Republican votes:", wasted_votes[1])
        # The misspelling of eligible is to comply with Submitty
        print(total_voters, "elgible voters")

        # Only continue if there are at least three districts
        if len(district_info) >= 3:
            # The efficiency gap calculation and gerrymandering verdict should only run if there are at least three districts
            # Calculate the efficiency gap and which party it favors
            efficiency_gap, favored_party = find_efficiency_gap(total_voters, wasted_votes[0], wasted_votes[1])
            # Determine if the state is gerrymandered
            gerrymandered = is_gerrymandered(efficiency_gap, EGTHRESHOLD)
            print("The Efficiency Gap is " + str(round(efficiency_gap * 100, 1)) + "% in favor of " + favored_party + ".")
            if gerrymandered:
                print("The State does appear to be gerrymandered.")
            else:
                print("The State does not appear to be gerrymandered.")
        else:
            # This is printed if there aren't enough districts to calculate an efficiency gap
            print("There are an insufficient number of districts to calculate an Efficiency Gap.")
            # The extra space between sentences is to comply with Submitty
            print("This State has", len(district_info), "districts.  States with less than three districts cannot be gerrymandered.")

        # Graph the districts to help visualize the data
        graph_districts(state_name, total_voters, district_info, WIDTH, HEIGHT)
        
    else:
        # Prints if the user input is not found within the districts.txt file
        print("\"" + input_state + "\" not found.")
        

"""
Takes user input, searches for an entry in districts.txt that matches,
and returns an array of the line split by commas
"""
def get_district_info(user_input, states_districts):
    for line in states_districts:
        state_name = line.split(",")[0].lower()
        if state_name == user_input.lower():
            return line.strip().split(",")
    return None


def get_voter_info(user_input, states_voters):
    for line in states_voters:
        # Both state_name and user input are lowercased to prevent case-errors from interfering with detection
        state_name = line.split(",")[0].lower()
        if state_name == user_input.lower():
            # Explanation for the string of methods and functions, in order:
            # .strip() removes the newline character (\n) if it exists, and any other whitespace if present
            # .split(",") splits the line into an array of elements split by every comma that appears
            # [-1] returns the last element, which contains the number of eligible voters in the state
            # int() converts the number of eligible voters from a string to an int
            return int(line.strip().split(",")[-1])
    return None

"""
This function takes the array of district info, including the numbered districts and state's name,
and converts it to an array of arrays, where each subarray represents a district and contains the 
integer values of each district's tally of Democrat and Republican votes
"""
def filter_districts(info):
    # This cuts out the first element of the array, the state name 
    raw_districts = info[1:]
    districts = []
    # Move by 3 each iteration, to save only the votes and not the number representing the district
    for d in range(0, len(raw_districts), 3):
        # Add a subarray of the number of democratic votes and the number of republican votes
        districts += [[int(raw_districts[d+1]), int(raw_districts[d+2])]]
    return districts


"""
Calculates the wasted votes for both the Republican and Democrat parties
"""
def find_waste(districts):
    # Initialize variables
    waste_dem = 0
    waste_rep = 0

    # For each district in the state
    for d in districts:
        if d[0] > d[1]:
            # If Democrats won the district
            # Any Democratic votes beyond half the total votes of the district plus one are wasted
            # All Republican votes are wasted
            waste_dem += d[0] - ((d[0] + d[1]) // 2 + 1)
            waste_rep += d[1]
        elif d[0] < d[1]:
            # If Republicans won the district
            # Any Republican votes beyond half the total votes of the district plus one are wasted
            # All Democratic votes are wasted
            waste_dem += d[0]
            waste_rep += d[1] - ((d[0] + d[1]) // 2 + 1)
        else:
            # If there is a tie (unlikely), the entirety of both parties' votes are wasted
            waste_dem += d[0]
            waste_rep += d[1]
    
    # Return both parties' wasted votes
    return [ waste_dem, waste_rep ]


"""
Calculates the efficiency gap and the party favored by it
"""
def find_efficiency_gap(votes, waste_dem, waste_rep):
    # Initialize the variable
    favor = None
    # Calculate the efficiency gap
    eff_gap = (waste_dem - waste_rep) / votes
    # Determine the party favored by the efficiency gap
    if eff_gap > 0:
        # If EG is positive, the Democrats wasted more votes
        favor = "the Republicans"
    elif eff_gap < 0:
        # If EG is negative, the Republicans wasted more votes
        favor = "the Democrats"
    else:
        # If efficiency gap is 0, rare but possible, especially in edge-case testing
        # This also makes formatting the overall string to print much easier
        favor = "neither party"
    
    # Return the efficiency gap and the favored party
    return abs(eff_gap), favor


"""
Determine if the efficiency gap meets or exceeds the given threshold
"""
def is_gerrymandered(eff_gap, threshold):
    # Create the boolean value
    gerrymandered = False
    # Determine if it meets or exceeds the threshold
    if eff_gap >= threshold:
        gerrymandered = True
    # Return whether or not the state is gerrymandered
    return gerrymandered


"""
Visualize the votes casted for both parties in each district in a given state
"""
def graph_districts(state, num_voters, districts, w, h):
    # Create canvas
    win = GraphWin("District Breakdown", w, h)

    # Create the horizontal line
    hori_line = Line(Point(0, 20), Point(w, 20))
    hori_line.draw(win)

    # Create the vertical line
    vert_line = Line(Point(w/2, 0), Point(w/2, h))
    vert_line.draw(win)

    # Create the text that displays the state name
    # Unfortunately, setting the text to (0,0) cuts most of it off
    # Moving the text right by four times the length of the string is the solution I found to consistently show all necessary info
    state_text = Text(Point(len(state) * 4,10), state)
    state_text.setSize(10)
    state_text.draw(win)

    # Create the text that displays eligible voters
    # Moving it left from the right edge by 120 pixels seems too far, but moving left from the right edge by 80 pixels seems to work
    voters_text = Text(Point(w-80, 10), str(num_voters) + " eligible voters")
    voters_text.setSize(10)
    voters_text.draw(win)

    # The top of the first bar is 25 pixels down, as per the instructions
    bar_top = 25
    # For every district
    for d in districts:
        # Calulate the length of the democratic bar
        try:
            democratic_bar_length = d[0] / (d[0] + d[1]) * w
        except ZeroDivisionError:
            # Added this try/except block because some districts have no votes for either party tallied (e.g. Florida)
            democratic_bar_length = w / 2

        # Create the bar that represents Democratic votes
        blue_bar = Rectangle(Point(0, bar_top), Point(democratic_bar_length, bar_top + 20))
        blue_bar.setFill("blue")
        blue_bar.setOutline("blue")
        blue_bar.draw(win)

        # Create the bar that represents Republican votes
        red_bar = Rectangle(Point(democratic_bar_length, bar_top), Point(w, bar_top + 20))
        red_bar.setFill("red")
        red_bar.setOutline("red")
        red_bar.draw(win)

        # Adding the length of the bar and the space in-between
        bar_top += 25

    # Wait until user clicks on the graph to close
    win.getMouse()
    win.close()

# Run the main function if this program is being run directly and not imported
if __name__ == "__main__":
    main()