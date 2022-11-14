#********************************************************************
#  RationalTester.py       Author: Originally Lewis/Loftus, converted to Python by Lex Baker
#
#  Driver to exercise the use of multiple Rational objects.
#********************************************************************

from RationalNumber import RationalNumber

def main():
    '''Creates some rational number objects and performs various operations on them.'''
    r1 = RationalNumber(6, 8)
    r2 = RationalNumber(1, 3)

    print("First rational number:", r1)
    print("Second rational number:", r2)

    if (r1.isLike(r2)):
        print("r1 and r2 are equal.")
    else:
        print("r1 and r2 are NOT equal.")
    r3 = r1.reciprocal()
    print("The reciprocal of r1 is:", r3)
    r4 = r1.add(r2)
    r5 = r1.subtract(r2)
    r6 = r1.multiply(r2)
    r7 = r1.divide(r2)
    print("r1 + r2:", r4)
    print("r1 - r2:", r5)
    print("r1 * r2:", r6)
    print("r1 / r2:", r7)


    if (r1.isLike(r2)):
        print("r1 and r2 are equal.")
    else:
        print("r1 and r2 are NOT equal.")

    r3 = r1.reciprocal()
    print("The reciprocal of r1 is:", r3)
    r4 = r1.add(r2)
    r5 = r1.subtract(r2)
    r6 = r1.multiply(r2)
    r7 = r1.divide(r2)
    print("r1 + r2:", r4)
    print("r1 - r2:", r5)
    print("r1 * r2:", r6)
    print("r1 / r2:", r7)


if __name__ == "__main__":
    main()

"""
Expected Output:

First rational number: 3/4
Second rational number: 1/3
r1 and r2 are NOT equal.
The reciprocal of r1 is: 4/3
r1 + r2: 13/12
r1 - r2: 5/12
r1 * r2: 1/4
"""