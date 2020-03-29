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
	def find_min(self):
		current = self
		while current.left is not None:
			current = current.left
		return current
	
	def next_larger(self):
		if self.right is not None:
			return self.right.find_min()
		current = self
		while current.parent is not None and current is current.parent.right:
			current = current.parent
		return current.parent	
		
	def delete(self):
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
			s = self.right
			self.val, s.val = s.val, self.val
			self._val, s._val = s._val, self._val
			return s.delete()
		
	def find(self, k):
		if k == self._val:
			return self
		elif k < self._val:
			if self.left is None:
				return None
		        else:
				return self.left.find(k)
		else:
			if self.right is None:  
				return None
			else:
				return self.right.find(k)	
class Node2:
	def __init__(self, bst, left = None, right = None, parent = None, height = 1, bf = 0):
		self.val = bst
		self.left = left
		self.right = right
		self.parent = parent
		self.height = height
		self.bf = bf
		self._val = bst.root._val[0]
		
	def find_min(self):
		current = self
		while current.left is not None:
			current = current.left
		return current
	
	def next_larger(self):
		if self.right is not None:
			return self.right.find_min()
		current = self
		while current.parent is not None and current is current.parent.right:
			current = current.parent
		return current.parent	
		
	def delete(self):
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
			s = self.right
			self.val, s.val = s.val, self.val
			self._val, s._val = s._val, self._val
			return s.delete()
		
	def find(self, k):
		if k == self._val:
			return self
		elif k < self._val:
			if self.left is None:
				return None
		        else:
				return self.left.find(k)
		else:
			if self.right is None:  
				return None
			else:
				return self.right.find(k)