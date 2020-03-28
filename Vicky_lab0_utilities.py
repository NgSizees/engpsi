class Word:
	def __init__(self, key, definition):
		self.name = key
		self.definition = definition
		

	def __str__(self):
		return self.name

class Node:
	def __init__(self, word, left = None, right = None, parent = None, height = 1, bf = 0):
		self.val = [word]
		self.left = left
		self.right = right
		self.parent = parent
		self.height = height
		self.bf = bf
		self._val = str(word)
	def delete(self):
		"""Deletes and returns this node from the tree."""
		if self.left is None or self.right is None:
			if self is self.parent.left:
				self.parent.left = self.left or self.right
				if self.parent.left is not None:
					self.parent.left.parent = self.parent
			else:
				self.parent.right = self.left or self.right
				if self.parent.right is not None:
					self.parent.right.parent = self.parent
			return self
		else:
			s = self.next_larger()
			self.key, s.key = s.key, self.key
			return s.delete()	
class Node2:
	def __init__(self, bst, left = None, right = None, parent = None, height = 1, bf = 0):
		self.val = bst
		self.left = left
		self.right = right
		self.parent = parent
		self.height = height
		self.bf = bf
		self._val = bst.root._val[0]
		
	def delete(self):
		"""Deletes and returns this node from the tree."""
		if self.left is None or self.right is None:
			if self is self.parent.left:
				self.parent.left = self.left or self.right
				if self.parent.left is not None:
					self.parent.left.parent = self.parent
			else:
				self.parent.right = self.left or self.right
				if self.parent.right is not None:
					self.parent.right.parent = self.parent
			return self
		else:
			s = self.next_larger()
			self.key, s.key = s.key, self.key
			return s.delete()
