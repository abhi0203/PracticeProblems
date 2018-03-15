# This is code written to find nth Fibo numbers.
# Problem statememt: How do you find a number at a particular location in Fibo series.
# Here I am assuming that location/ position starts from 0.
# @Author: Abhiram
# Date: 15-March

#Solution for O(n) and constant space complexity
fiboList=[0,1]
def calcFiboSimple(pos):
	if pos<2 and pos>=0:
		return pos
	slast=0
	last=1
	currentPos= last+1
	while currentPos<= pos:
		temp= last
		last= slast + last
		slast= temp
		currentPos+=1
	return last

def calcFiboRecursive(pos):
	currentPos= len(fiboList)
	if pos< currentPos:
		return fiboList[pos]
	else:
		fiboList.append(calcFiboRecursive(pos-1) + calcFiboRecursive(pos-2))
		return fiboList[-1]

print(calcFiboSimple(20))
calcFiboRecursive(20)
print(fiboList[-1])
