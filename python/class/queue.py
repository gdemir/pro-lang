class Queue:
	def __init__(self):
		self.list = []

	def isEmpty(self):
		return self.list == []

	def enqueue(self, item):
		self.list.append(item)

	def dequeue(self):
		self.list.pop(0)

	def size(self):
		return len(self.list)
