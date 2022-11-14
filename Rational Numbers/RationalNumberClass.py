#*******************************************************************************************
#  RationalNumber.py       Author: Originally Lewis/Loftus, converted to Python by Lex Baker
#
#  Represents one rational number with a numerator and denominator.
#*******************************************************************************************

class RationalNumber:
    '''Represents one rational number with a numerator and denominator.'''

    def __gcd__(self, num1, num2):
        '''Computes and returns the greatest common divisor of the two
        positive parameters. Uses Euclid's algorithm.'''
        while (num1 != num2):
            if (num1 > num2):
                num1 = num1 - num2
            else:
                num2 = num2 - num1
        return num1

    def __init__(self, numer, denom):
        '''Constructor: Sets up the rational number by ensuring a nonzero
        denominator and making only the numerator signed. Non-integers are converted.'''
        self.numerator = numer
        self.denominator = denom

        if (denom == 0):
            denom = 1
        # Make the numerator "store" the sign
        if (denom < 0):
            numer = numer * -1
            denom = denom * -1

        self.numerator = numer
        self.denominator = denom
        self.__reduce__()
    
    def __reduce__(self):
        '''Reduces this rational number by dividing both the numerator
        and the denominator by their greatest common divisor.'''
        if (self.numerator != 0):
            common = self.__gcd__(abs(self.numerator), self.denominator)
            self.numerator = self.numerator // common
            self.denominator = self.denominator // common

    def __str__(self):
        result = ""
        if (self.numerator == 0):
            result = "0"
        else:
            if (self.denominator == 1):
                result = str(self.numerator) + ""
            else:
                result = str(self.numerator) + "/" + str(self.denominator)
        return result

    def getNumerator(self):
        '''Returns the numerator of this rational number.'''
        return self.numerator

    def getDenominator(self):
        '''Returns the denominator of this rational number.'''
        return self.denominator

    def reciprocal(self):
        '''Returns the reciprocal of this rational number.'''
        return RationalNumber(self.denominator, self.numerator)

    def add(self, op2):
        '''Adds this rational number to the one passed as a parameter. A common 
        denominator is found by multiplying the individual denominators.'''
        commonDenominator = self.denominator * op2.getDenominator()
        numerator1 = self.numerator * op2.getDenominator()
        numerator2 = op2.getNumerator() * self.denominator
        sum = numerator1 + numerator2
        return RationalNumber(sum, commonDenominator)
    
    def subtract(self, op2):
        '''Subtracts the rational number passed as a parameter 
        from this rational number.'''
        commonDenominator = self.denominator * op2.getDenominator()
        numerator1 = self.numerator * op2.getDenominator()
        numerator2 = op2.getNumerator() * self.denominator
        difference = numerator1 - numerator2
        return RationalNumber(difference, commonDenominator)

    def multiply(self, op2):
        '''Multiplies this rational number by the one passed as a parameter.'''
        numer = self.numerator * op2.getNumerator()
        denom = self.denominator * op2.getDenominator()
        return RationalNumber(numer, denom)

    def divide(self, op2):
        '''Divides this rational number by the one passed as a parameter
        by multiplying by the reciprocal of the second rational.'''
        return self.multiply(op2.reciprocal())
    
    def isLike(self, op2):
        '''Determines if this rational number is equal to the one passed
        as a parameter. Assumes they are both reduced.'''
        return ( self.numerator == op2.getNumerator() and self.denominator == op2.getDenominator() )