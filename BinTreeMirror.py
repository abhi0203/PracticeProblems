# This code check if the Binary tree is mirror image of each other.
# Author Abhiram
# Date: March 21

'''
Algorithm

- Start with root node. Use BFS
- Put first item in queue.
- Call recursive mirror function.
- In the recursive function
	- If queue is empty, return true.
	- Create 2 lists to hold objects and values.
	- While queue is not empty
		- get the object.
		- insert value in first list
		- insert object in other list.
	- Check if the list and reverse are same. If it is, this level is mirror image.
		- get each object from object list and check if they have children.
		- If they have, insert into queue.
		- Call the mirror function recursively.
	- else
		- They are not mirror imace
		- return False
	return True

'''
import queue

class node:
	def __init__(self, value= None):
		self.value= value
		self.leftChild= None
		self.rightChild= None

	def bfs(self):
		if self== None:
			print("Tree is empty")
		else:
			bfsQueue= queue.Queue()
			bfsQueue.put(self)
			return self._isMirror(bfsQueue)

	def _isMirror(self, bfsQueue):
		if bfsQueue.empty():
			return True
		objList=[]
		objValList= []
		while not bfsQueue.empty():
			obj= bfsQueue.get()
			objList.append(obj)
			objValList.append(obj.value)
		if objValList== objValList[::-1]:
			for data in objList:
				if data.leftChild:
					bfsQueue.put(data.leftChild)
				if data.rightChild:
					bfsQueue.put(data.rightChild)
			if self._isMirror(bfsQueue):
				return True
			else: 
				return False
		else:
			return False

# Helper Code
tree= node(5)
l1= node(6)
l2= node(6)
l3= node(7)
l4= node(8)
l5= node(8)
l6= node(7)
tree.leftChild= l1
tree.rightChild= l2
l1.leftChild= l3
l1.rightChild= l4
l2.leftChild= l5
l2.rightChild= l6
print(tree.bfs())

