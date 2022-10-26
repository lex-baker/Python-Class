from graphics import *

WIDTH = 500
HEIGHT = 500
EGTHRESHOLD = .07

districts = open("districts.txt").readlines()

voters = open("eligible_voters.txt").readlines()

def main():
    input_state = input("Enter a state to find if it's gerrymandered: ")
    print(input_state)
    raw_district_info = get_district_info(input_state)
    if raw_district_info != None:
        state_name = raw_district_info.split(",")[0]
        total_voters = get_voter_info(input_state)
        #is_gerrymandered(voter_info[0], voter_info[1], district_info)
        #print information
        #draw graph
        
    else:
        print(f"\"{input_state}\" not found.")
        

    """
    Which state do you want to look up? Arizona
    Total Wasted Democratic votes: 327852
    Total Wasted Republican votes: 369697
    4738332 eligible voters
    The Efficiency Gap is 0.9% in favor of the Democrats.
    The State does not appear to be gerrymandered.
    """

def get_district_info(user_input):
    district_info = None
    voter_info = None
    for line in districts:
        state_name = line.split(",")[0].lower()
        if state_name == user_input.lower():
            district_info = line
            print(district_info)
            return district_info
    return None

def get_voter_info(user_input):
    for line in voters:
        state_name = line.split(",")[0].lower()
        if state_name == user_input.lower():
            voter_info = line.split(",")[1]
            print(voter_info)
            return voter_info
    return None

def is_gerrymandered(state, num_voters, state_district):
    print()
    

def graph_districts():
    win = GraphWin("District Breakdown", WIDTH, HEIGHT)


main()