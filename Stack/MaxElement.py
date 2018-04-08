'''
This is the problem from hacker rank.
Here were are supposed to create a stack and implement below features.
	- From the command line we will enter 2 types of inputs.
		- First will be N which represents N test cases.
		- Second will be N test cases which will represent either one of the operation.
			1) 2 integers separated by sapce. First is 1 and second is number to be pushed on stack.
			2) One integer 2 which means we need to pop the element.
			3) One integer 3 which means we need to return max element of the stack.

There are 2 ways we can implement this. Note that Push and pop functions remains the same.

1) We create a simple stack using a list. We then use list's max function to return the max value.
   Though this is the simplest method, it does not work well for large input sets. Finding max is of O(n)
2) We calculate the max only at the time of inserting into the stack. 
	- So we set integer variable to min int value.
	- Then everytime we push into the stack we check if the value is greater. If yes, we set the max variable to this value.
	- Everytime we pop, we check if the popped item is max value. If not okay. If it is, and if the stack is not empty, we 
	  set the max value to max value in the list using list's max function. If the stack is empty, then we again set 
	  max value to min integer value.
'''
# Author Abhiram
# Date: 07-April

import sys
class Stack:
	def __init__(self):
		self.items=[]
		self.curmax= -sys.maxsize
	
	def push(self, value):
		self.items.append(value)
		if value> self.curmax:
			self.curmax= value

	def pop(self):
		value= self.items.pop()
		if value== self.curmax:
			if not self.isEmpty():
				self.curmax= max(self.items)
			else:
				self.curmax= -sys.maxsize
		return value

	def isEmpty(self):
		return self.items==[]

	def maxValue(self):
		return self.curmax



N= int(input())
s= Stack()
for _ in range(N):
	case= input()
	case= case.split() 
	if int(case[0])==1:
		s.push(int(case[1]))
	elif int(case[0])==2:
		s.pop()
	elif int(case[0])==3:
		print(s.maxValue())
