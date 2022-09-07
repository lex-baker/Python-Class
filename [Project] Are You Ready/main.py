#########################
# Author: Lex Baker
# Date: 9/3/22
# This program takes several user inputs and calculates how prepared they are for an upcoming event
#########################

def main():
    # Input
    # Variables S, C, and P_N are used in the numerator calculations
    # Hours of sleep
    S = eval(input("Hours of sleep you had last night: "))
    print(S)
    # Shots of stimulants
    C = eval(input("Shots of espresso or other stimulants consumed: "))
    print(C)
    # Hours of prep needed for the event
    P_N = eval(input("Hours of preparation needed to excel: "))
    print(P_N)
    # Variables P_A, D, N, and I are used in the denominator calculations
    # Hours spent preparing
    P_A = eval(input("Hours you actually spent preparing: "))
    print(P_N)
    # Difficulty of subject matter
    D = eval(input("Difficulty of the subject matter (1 - 10 with 10 being \'theoretical particle physics\'): "))
    if(D < 1 or D > 10):
        print("Input is invalid")
        exit()
    print(D)
    #Level of nervousness
    N = eval(input("Level of nervousness ( 1 - 10 with 10 being \'tightrope across the grand Canyon on a windy day\'): "))
    if(N < 1 or N > 10):
        print("Input is invalid")
        exit()
    print(N)
    # Importance of Event (1-10)
    I = eval(input("Importance of the event (1 - 10 with 10 being \'singing the national anthem at the Super Bowl\'): "))
    if(I < 1 or I > 10):
        print("Input is invalid")
        exit()
    print(I)

    # Processing
    


main()