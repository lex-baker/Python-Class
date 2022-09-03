#########################
# Author: Lex Baker
# Date: 8/31/22
# This program calculates six functions using two user-inputted numbers: add, subtract, multiply, integer division, division, and modulus
#########################

# Initialize
def main():
    # Get the user input
    in_1 = eval(input("Enter a value: "))
    print(in_1)
    in_2 = eval(input("Enter a second value: "))
    print(in_2)

    # Process and Output
    # Print the calculated values

    # Addition
    print(in_1, "+", in_2, "=", in_1 + in_2)

    # Subtraction
    print(in_1, "-", in_2, "=", in_1 - in_2)

    # Multiplication
    print(in_1, "*", in_2, "=", in_1 * in_2)

    # Integer divison
    print(in_1, "//", in_2, "=", in_1 // in_2)

    # Division
    print(in_1, "/", in_2, "=", in_1 / in_2)

    # Modulus
    print(in_1, "%", in_2, "=", in_1 % in_2)

    #Terminate

main()