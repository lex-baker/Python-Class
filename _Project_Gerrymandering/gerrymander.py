from re import S
from graphics import *

districts = open("districts.txt").readlines()

voters = open("eligible_voters.txt").readlines()

def main():
    input_state = input("Enter a state to find if it's gerrymandered: ").lower()
    district_info = None
    voter_info = None
    for line in districts:
        state_name = line.split(",")[0].lower()
        if state_name == input_state:
            district_info = line
            print(district_info)
            break
    
    for line in voters:
        state_name = line.split(",")[0].lower()
        if state_name == input_state:
            voter_info = line
            print(voter_info)
            break

    if district_info == None or voter_info == None: 
        print(input_state + " is not a state")
    else:
        gerrymander(voter_info[0], voter_info[1], district_info)


def gerrymander(state, num_voters, state_district):
    print()
    win = GraphWin("Title", )


main()