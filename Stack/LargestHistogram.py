'''
This is the problem from Hacker Rank. Here we have been given an array that represent the height of the histogram with unit width.
We need to find the largest rectangle that can be formed from the histogram.

Method 1: 
Brute Force way. However this way we actually solve the problem in O(n^2)
- We pick each index.
- Then we traverse left from that point till either we exhaust the historgram or we find an value less than current index. While we traverse, we keep the count of data points we traverse.
- Then we traverse left for the same condition and also keep the count.
- Once the traversing is done, we calculate the current area using currArea= height*(leftCount+ rightCount+1)
- If the currArea is greater than Area then we replace else not.
- We repeat the same process for all the items in the array and finally return the area. 
'''

'''
Method 2:
This is the method where we use Stack and try to reduce the time complexity of the code.
So we start traversing the list. 
- As we encounter an item from the list, if the stack is empty or top value of stack is <= currentListItem we push it to the stack.
- As we encounter an item whichs is less than top of stack, we stop, we then pop the stack till we encounter an item less than current top of stack. We then calculate the area for that part.
  We also increment the popped item count and then later on use that to calculate the area for remaining items.

'''
#Author Abhiram Pattarkine
# Date: 24-May


import math
import os
import random
import re
import sys

class Stack:

	def __init__(self):
		self.items=[]

	def push(self, value):
		self.items.append(value)

	def pop(self):
		return self.items.pop()

	def peek(self):
		if self.isempty():
			return -1
		return self.items[-1]

	def isempty(self):
		return self.items==[]


# Complete the largestRectangle function below.
def largestRectangleBruteForce(h):
    globalArea=0
    for i in range(len(h)):
        leftCount=0
        rightCount=0
        leftIndex= i-1 
        rightIndex=i+1
        currArea=0
        while leftIndex>=0 and h[leftIndex]>= h[i]:
            leftCount+=1
            leftIndex-=1
        while rightIndex<len(h) and h[rightIndex]>= h[i]:
            rightCount+=1
            rightIndex+=1
        currArea= h[i]* (leftCount+ rightCount +1)
        if currArea>globalArea:
            globalArea= currArea
    return globalArea

def largestRectangle(h):
    globalArea=0
    s= Stack()
    for i in range(len(h)):
        if s.isempty() or s.peek()[1]<= h[i]:
            s.push([i,h[i]])
            continue
        else:
            while not s.isempty() and s.peek()[1]> h[i]:
                currArea=0
                popCount= 0
                data= s.pop()
                currItem= data[1]
                popCount=1
                while not s.isempty() and currItem<= s.peek()[1]:
                    temp=s.pop()
                    popCount=1+ (data[0]- temp[0])
                currArea= currItem*popCount
                if currArea> globalArea:
                    globalArea= currArea
            s.push([i,h[i]])
    popCount=0
    while not s.isempty():
        currItem= s.pop()
        popCount=1
        while not s.isempty() and currItem<=s.peek()[1]:
            data= s.pop()
            currItem= data[1]
            popCount=1 + (data[0]- s.peek()[0])
        currArea= currItem * popCount
        if currArea> globalArea:
            globalArea= currArea

    return globalArea


    

h=[2,3,4,2,1,2,4,5,5,6,3,2,12,3,2,1,4,5,2,1]
print(largestRectangleBruteForce(h))
print(largestRectangle(h))






'''
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    h = list(map(int, input().rstrip().split()))

    result = largestRectangle(h)

    fptr.write(str(result) + '\n')

    fptr.close()

'''


