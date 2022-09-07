#########################
# Author: Lex Baker
# Date: 9/6/22
# This program calculates how many grains of rice the mathematician would have in the Chess Problem
#########################

def main():
    grains = 0
    for x in range(64):
        grains += 2**x
    print(grains)
    


main()