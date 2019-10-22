class Node:

	def __init__(self, val):
		self.value = val
		self.left_child = None
		self.right_child = None

	def insert(self, data):
		if (self.value == data):
			return False
		elif self.value > data:
			if self.left_child:
				return self.left_child.insert(data)
			else:
				self.left_child = Node(data)
				return True
		else:
			if self.right_child:
				return self.right_child.insert(data)
			else:
				self.right_child = Node(data)
				return True

	def find(self, data):
		if self.value == data:
			return True
		elif self.value > data:
			if self.left_child:
				return self.left_child.find(data)
			else:
				return False
		else:
			if self.right_child:
				return self.right_child.find(data)
			else:
				return False

	def preorder(self):
		if self:
			print(str(self.value))
			if self.left_child:
				self.left_child.preorder()
			if self.right_child:
				self.right_child.preorder()

	def postorder(self):
		if self:
			# print(str(self.value))
			if self.left_child:
				self.left_child.postorder()
			if self.right_child:
				self.right_child.postorder()
			print(str(self.value))

	def inorder(self):
		if self:
			if self.left_child:
				self.left_child.inorder()
			print(str(self.value))
			if self.right_child:
				self.right_child.inorder()
			


class Tree:

	def __init__(self):
		self.root = None

	def insert(self, data):
		# if root node exist
		if self.root:
			return self.root.insert(data)
		else:
			self.root = Node(data)
			return True

	def find(self, data):
		if self.root:
			return self.root.find(data)
		else:
			return False

	def preorder(self):
		print('Preorder')
		self.root.preorder()

	def postorder(self):
		print('Postorder')
		self.root.postorder()

	def inorder(self):
		print('Inorder')
		self.root.inorder()

howard = Tree()
howard.insert(10)
# print(howard.insert(15))










