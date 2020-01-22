
class CompoundFraction():

    ##### Problem 1 #####
    def __init__(self, wholeNumber, numerator, denominator):
        self.wholeNumber=wholeNumber
        self.numerator=numerator
        self.denominator=denominator


    ##### Problem 2 #####
    def __repr__(self):
        #both of these work
        #return "{} and {}/{}".format(self.wholeNumber, self.numerator, self.denominator)
        return "{self.wholeNumber} and {self.numerator}/{self.denominator}".format(self=self)

    
    ##### Problem 3 #####
    def __float__(self):
        return float(self.wholeNumber) + float(self.numerator)/float(self.denominator)


    ##### Problem 4 #####
    def __eq__(self, cf2):
        return self.__float__() == cf2.__float__()

    
    ##### Problem 5 #####
    def isSimplified(self):
        if self.numerator < 0 or self.denominator<self.numerator:
            return False
        for i in range(2, self.numerator):
            if self.numerator%i==0 and self.denominator%i==0:
                return False
        return True

if __name__ == "__main__":
    import doctest
    print(doctest.testfile('hw7_test.py', verbose=False))
        
  