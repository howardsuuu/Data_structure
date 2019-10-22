class Node():
	"""docstring for Box"""

	def __init__(self, data):
		
		self.data = data
		self.next = None

	# def count_node(head):
	# 	count = 1
	# 	now = head
	# 	while head.next_data is not None:
	# 		 now = now.next_data
	# 		 count += 1
		# return count


class Node_adding():

	def __init__(self):

		self.head = None
		self.tail = self.head

	def add_node(self, val):

		if self.head is None:
			self.head.data = val
			self.tail = self.head
		else:
			new_node = Node(val)
			self.tail.next = new_node
			self.tail = new_node




def helper():
	val = int(input('Enter Number: '))
	return Node_adding().add_node(val)

helper()









# nodeA = Node(6)
# nodeB = Node(3)
# nodeC = Node(4)
# nodeD = Node(2)
# nodeE = Node(1)

# nodeA.next_data = nodeB
# nodeB.next_data = nodeC
# nodeC.next_data = nodeD
# nodeD.next_data = nodeE