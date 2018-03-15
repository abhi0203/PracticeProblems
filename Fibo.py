# This is code written to find nth Fibo numbers.
# Problem statememt: How do you find a number at a particular location in Fibo series.
# Here I am assuming that location/ position starts from 0.
# @Author: Abhiram
# Date: 15-March

#Solution for O(n) and constant space complexity
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

def calcFiboRecursive(pos, lst):
	currentPos= len(lst)
	if pos<= len(lst)-1:
		return lst
	while currentPos<=pos:
		lst[currentPos].append(calcFiboRecursive(currentPos-1, lst) + calcFiboRecursive(currentPos-2, lst))
		currentPos+=1
	return lst



print(calcFiboSimple(5))
print(calcFiboRecursive(5,[0,1])[-1])
