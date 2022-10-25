from graphics import *

WIDTH = 500
HEIGHT = 500
EGTHRESHOLD = .07

districts = open("districts.txt").readlines()

voters = open("eligible_voters.txt").readlines()

def main():
    input_state = input("Enter a state to find if it's gerrymandered: ")
    district_info = get_district_info(input_state)
    voter_info = get_voter_info(input_state)
    if district_info == None or voter_info == None: 
        print(input_state + " is not a state")
        
    else:
        is_gerrymandered(voter_info[0], voter_info[1], district_info)

def get_district_info(user_input):
    district_info = None
    voter_info = None
    for line in districts:
        state_name = line.split(",")[0].lower()
        if state_name == user_input.lower():
            district_info = line
            print(district_info)
            break
def get_voter_info(user_input):
    for line in voters:
        state_name = line.split(",")[0].lower()
        if state_name == user_input.lower():
            voter_info = line
            print(voter_info)
            break

def is_gerrymandered(state, num_voters, state_district):
    print()
    

def graph_districts():
    win = GraphWin("District Breakdown", WIDTH, HEIGHT)


main()