initial_size = 50

class Node:
	def __init__(self, key, value):
		self.key = key
		self.value = value
		self.next = None

class HashTable:
	def __init__(self):
		self.capacity = initial_size
		self.size = 0
		self.buckets = [None]*self.capacity

	def hash(self, key):
		hashsum = 0

		for index, x in enumerate(key):
			hashsum += (index + len(key)) ** ord(x)
			hashsum = hashsum % self.capacity

		return hashsum

	def add(self, key, value):
		self.size += 1
		index = self.hash(key)
		node = self.buckets[index]

		if node is None:
			self.buckets[index] = Node(key, value)
			return

		prev = node

		while node is not None:
			prev = node
			node = node.next

		prev.next = Node(key, value)

	def get(self, key):
		index = self.hash(key)
		node = self.buckets[index]

		while node is not None and node.key != key:
			node = node.next
		if node is None:
			return None
		else:
			return node.value

	def contains(self, key):
		index = self.hash(key)
		node = self.buckets[index]

		if node == None:
			return False
		else:
			return True