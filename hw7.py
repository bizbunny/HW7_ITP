#Collaborator: Vi-Linh Nguyen
#HW7
#Problem 1
class CompoundFraction:
	def __init__(self,wholeNumber,numerator,denominator):
		self.wholeNumber=wholeNumber
		self.numerator=numerator
		self.denominator=denominator
#Problem 2
	def __repr__(self):
		return(str(self.wholeNumber)+' and '+str(self.numerator)+'/'+str(self.denominator))	
#Problem 3
	def __float__(self):
		return(self.wholeNumber+(self.numerator/self.denominator))
#Problem 4
	def __eq__(self, other):
		if(float(self.wholeNumber+(self.numerator/self.denominator))==float(other.wholeNumber+(other.numerator/other.denominator))):
			return True
		else:
			return False
#Problem 5
	def isSimplified(self):
		if (0<=self.numerator<=self.denominator):
			for i in range(2,10):
				if(self.numerator%i==0 and self.denominator%i==0):
					return False
			return True
		else:
			return False	
if __name__ == "__main__":
    import doctest
    print(doctest.testfile('hw7_test.py', verbose=False))
