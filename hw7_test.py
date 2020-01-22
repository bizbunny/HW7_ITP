
>>> from hw7 import *

NOTE: We will be creating a single class CompundFraction in this homework. Each problem will add onto the methods available.
NOTE: a compoundFraction "1 and 2/3" has wholeNumber==1, numerator==2, and denominator==3

##### Problem 1 #####

Create a class CompoundFraction with a constructor that takes as input 3 instance variables -- wholeNumber, numerator, and denominator.

>>> cf = CompoundFraction(1, 2, 3)
>>> cf.wholeNumber==1 and cf.numerator==2 and cf.denominator==3
True
>>> cf = CompoundFraction(0, 5, 6)
>>> cf.wholeNumber==0 and cf.numerator==5 and cf.denominator==6
True


##### Problem 2 #####

Add a __repr__ method to CompoundFraction so that print() will print it in a user-friendly format.

>>> cf = CompoundFraction(3, 4, 5)
>>> print(cf)
3 and 4/5
>>> print(CompoundFraction(0, 5, 6))
0 and 5/6
>>> print(CompoundFraction(1000, 2, 3))
1000 and 2/3


##### Problem 3 #####

Add a __float__ method to CompoundFraction so that float(cf) will return the compound fraction as a Float.

>>> cf = CompoundFraction(1, 3, 3)
>>> float(cf)
2.0
>>> float(CompoundFraction(0, 5, 8))
0.625
>>> float(CompoundFraction(1000, 2, 4))
1000.5


##### Problem 4 ######

Add a __eq__ method to CompoundFraction to check equality with other compound fractions
NOTE: It might be easiest to handle these by using the floating point value of CompoundFraction

>>> CompoundFraction(0, 4, 8) == CompoundFraction(0, 1, 2)
True
>>> CompoundFraction(0, 12, 4) == CompoundFraction(2, 2, 2)
True
>>> CompoundFraction(0, 12, 4) == CompoundFraction(3, 0, 1)
True
>>> CompoundFraction(0, 3, 4) == CompoundFraction(0, 7, 8)
False
>>> CompoundFraction(0, 3, 4) == CompoundFraction(1, 3, 4)
False


##### Problem 5 #####

Add an isSimplified() method to CompoundFraction that will return True if the compound fraction is simplified, otherwise False

NOTE: a compound fraction is simplified if 

1) the numerator is less than the denominator not negative (0<=numerator<=denominator)
2) the numerator and denominator cannot both be evenly divided any number greater than 1

>>> CompoundFraction(0, 4, 8).isSimplified()
False
>>> CompoundFraction(0, 1, 2).isSimplified()
True
>>> CompoundFraction(0, 3, 2).isSimplified()
False
>>> CompoundFraction(1, 1, 2).isSimplified()
True
>>> CompoundFraction(2, 9, 7).isSimplified()
False
>>> CompoundFraction(3, 2, 7).isSimplified()
True