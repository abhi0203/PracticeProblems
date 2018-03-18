# This is the code for solving the N queen problem.
# We have been given an n*n chess board and we have to arrange the queens in such a way that they dont attack each other.
# @ Author Abhiram
# Date: 16-March

'''
Input: n represents the rows and columns of the board and number of queens.
Output: List of tuples that represent x and y coordinates of 2D array which are nothing but positions of the quene.
		If the queens cannot be placed then return None
Rule: Tow or more queens should not be placed in row or column or in a diagonal.
Algorithm:
- Traverse first column wise and then row wise.
Step 1: Place a queen in first row and column. This is done by pushing the co-ordinates into the stack.
Step 2: Check if the queen is attacked. 
	Step 2.1: If not attacked, then move to next column and place the push the co-ordinates into stack.
			Step 2.1.1: Move onto next column and repeat.
	Step 2.2: If attacked, move to next row, push the co-ordinates and check if the queen is attacked. 
			Step 2.2.2: If all the rows are attacked then pop the columns

'''

#This is a function to check if the queen is attacked.
# Rule 1: The x co-ordinate should not be same. i.e should not be in same row.
# Rule 2: The y co-ordinate should nto be same. i.e should not be in same column.
# Rule 3: The absolute difference of x co-ordinate and y co-ordinate should not be same i.e. not in same diagonal

currentCoordinateList=[]

def checkIfAttacked(currentCoordinateList, currentQueenPosition):
	if len(currentCoordinateList)==0:
		return True
	for data in currentCoordinateList:
		if currentQueenPosition[0]== data[0] or currentQueenPosition[1]== data[1] or abs(currentQueenPosition[0]- data[0])==abs(currentQueenPosition[1]-data[1]):
			print("Attacks for")
			print(currentQueenPosition)
			return False
	return True

def placeQueen(n,row, column):
	if row==n and len(currentCoordinateList)==n:
		return True
	while row< n:
		currentCoordinateList.append((row,column))
		print("List After appending")
		print(currentCoordinateList)
		if checkIfAttacked(currentCoordinateList[:-1],(row,column)):
			if placeQueen(n,row+1,0):
				return True
			else:
				column+=1
				currentCoordinateList.pop()
				print("List after popping and column exhaustion")
				print(currentCoordinateList)
				if column==n:
					return False
		else:
			#Code for further column operation.
			column+=1
			currentCoordinateList.pop()
			print("List after normal popping")
			print(currentCoordinateList)
			if column==n:
				print(currentCoordinateList)
				return False

print(placeQueen(6,0,0))

