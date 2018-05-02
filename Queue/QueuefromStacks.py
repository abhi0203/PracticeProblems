'''
This is the code where I implement a queue from 2 stacks.
Stack is LIFO structure where as Queue is FIFO structure. So in order to implement dequeue function using stacks, we have to have the element we entered as first at the bottom of stack 1 as the element at the top. This is where the second stack going to come handy.

So as long as we have enqueue function, we keep pushing on stack 1. Once we encounter first dequeue function, assuming stack 2 is empty, we pop all items from stack1 and push them on stack2, and then pop the top item from stack 2.

Then as long as we have dequeue action, we keep popping from stack 2 till it is empty. All enqueue action still happen on stack 1.
'''
# Author: Abhiram
# Date 02-May

class Stack:
	def __init__(self):
		self.items=[]

	def push(self, value):
		self.items.append(value)

	def pop(self):
		return self.items.pop()

	def isEmpty(self):
		return self.items==[]

	def printStack(self):
		print(self.items)


class Queue:
	def __init__(self):
		self.stack1= Stack()
		self.stack2= Stack()

	def enqueue(self, value):
		self.stack1.push(value)

	def dequeue(self):
		if self.stack2.isEmpty():
			while not self.stack1.isEmpty():
				self.stack2.push(self.stack1.pop())
		return self.stack2.pop()

	def printQueue(self):
		self.stack1.printStack()
		self.stack2.printStack()


q= Queue()

q.enqueue(5)
q.enqueue(6)
q.enqueue(7)
q.enqueue(8)
q.dequeue()
q.printQueue()
q.enqueue(9)
q.enqueue(10)
q.enqueue(11)
q.printQueue()
