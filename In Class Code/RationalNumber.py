class RationalNumber:
    def __init__(self, num, den):
        self.numerator = num
        self.denominator = den

    def getNumerator(self):
        return self.numerator

    def getDenominator(self):
        return self.denominator

    def reciprocal(self):
        pass

    def add(self, op2):
        pass
    
    def subtract(self, op2):
        pass

    def multiply(self, op2):
        return RationalNumber(self.numerator * op2.getNumerator(), self.denominator * op2.getDenominator())

    def divide(self, op2):
        pass
    
    def find_gcf(self):
        pass

    def reduce(self):
        pass

    def __repr__(self):
        return str(self.numerator) + " / " + str(self.denominator) 



def main():
    r1 = RationalNumber(3, 4)
    print(r1)


if __name__ == "__main__":
    main()