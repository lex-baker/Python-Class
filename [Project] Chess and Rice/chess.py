#########################
# Author: Lex Baker
# Date: 9/6/22
# This program calculates how many grains of rice the mathematician would have in the Chess Problem
# Returned values are short formatted within the text, and given in full in parentheses following the text
#########################

# Defining the constants
# All variable names should be easy to understand, if there's any confusion, refer to the README
chess_squares = 64
grains_per_cup = 9619 
cups_per_cubic_mile = 1.762e13 # Python allows for the use of scientific notation
surface_area_sc = 32020 # This is in square miles
# Additional constants for bonus work
grams_per_cup = 202
grams_per_ton = 1e6
china_tons_produced = 2.1284e8
japan_tons_produced = 7.56e6

def main():
    # Running the accumulator
    grains = 0
    for x in range(chess_squares):
        grains += 2**x
    print("The mathematician would receive {0:.2e} grains of rice ({0})".format(grains))

    # Converting to cups
    cups = grains / grains_per_cup
    print("Which equals {0:.2e} cups of rice ({0})".format(cups))

    # Converting to cubic miles
    cubic_miles = cups / cups_per_cubic_mile
    print("That converts to", round(cubic_miles, 2), "cubic miles of rice", "({})".format(cubic_miles))

    # Dividing by surface area of South Carolina
    final_miles = cubic_miles / surface_area_sc

    # Adding 15% "void" space to the otherwise solid block of rice
    final_miles += final_miles * 0.15

    # Converting to feet
    final_feet = final_miles * 5280
    print("That converts to the final height in feet: {0:.2f} ({0})".format(final_feet))

    print("Bonus Work:")

    china_cups_produced = (china_tons_produced * grams_per_ton) / grams_per_cup
    print("China produced {0:.2e} cups of rice in 2021 ({0})".format(china_cups_produced))

    japan_cups_produced = (japan_tons_produced * grams_per_ton) / grams_per_cup
    print("Japan produced {0:.2e} cups of rice in 2021 ({0})".format(japan_cups_produced))

    cups_remaining = cups - china_cups_produced
    print("China would have {0:.2e} cups remaining ({0})".format(cups_remaining))

    cups_remaining = cups - japan_cups_produced
    print("Japan would have {0:.2e} cups remaining ({0})".format(cups_remaining))

    cups_remaining = cups - (china_cups_produced + japan_cups_produced)
    print("Together, China and Japan would have {0:.2e} cups remaining ({0})".format(cups_remaining))

    years_to_produce = cups / (china_cups_produced + japan_cups_produced)
    print("Assuming a stagnant yearly production rate, it would take China and Japan {0:.2f} years to produce enough rice for the mathematician ({0})".format(years_to_produce))

main()