class LinkList:
	class Node:
		# teta(1)
		def __init__(self, prev = None, next = None, value = None):
			self.prev = prev
			self.next = next
			self.value = value
	
	# teta(1)
	def __init__(self):
		self.head = self.Node()
		self.tail = self.Node(prev = self.head)
		self.head.next = self.tail
		self.count = 0

	# teta(1)
	def size(self):
		return self.count
	
	# teta(1)
	def isEmpty(self):
		return self.count<=0
	
	# teta(n)
	def each(self, action):
		node = self.head.next
		while node and node != self.tail:
			action(node.value)
			node = node.next
		return node
	
	# teta(n)
	def print(self):
		print("[ ", end="")
		self.each(lambda el: print(el, end=", "))
		print("]")

	# teta(i)
	def getNode(self, i):
		if not i in range(0, self.count): raise Exception('Out of Range')
		node = self.head
		for _ in range(0, i+1): node = node.next
		return node
	
	# teta(i)
	def get(self, i):
		return self.getNode(i).value

	# teta(i)
	def set(self, i, val):
		node = self.getNode(i) # teta(i)
		el = node.value
		node.value = val
		return el
	
	# O(i) Omega(1)
	def add(self, i, val):
		prev, next = None, None
		if i == 0: # teta(1)
			prev = self.head
			next = prev.next
		elif i == self.count: # teta(1)
			next = self.tail
			prev = next.prev
		else: # teta(i)
			next = self.getNode(i)
			prev = next.prev
		node = self.Node(prev=prev, next=prev.next, value=val)
		prev.next = node
		next.prev = node
		self.count += 1
		return node
	
	# teta(i)
	def remove(self, i):
		node = self.getNode(i)
		node.prev.next = node.next
		node.next.prev = node.prev
		self.count -= 1
		return node.value
	



#### TEST ####
def testLinkList():
	lst = LinkList()
	lst.print()
	lst.add(0, 1374)
	lst.print()
	lst.add(0, 1379)
	lst.print()
	lst.add(2, 1382)
	lst.print()

	for i in range(100, 1000, 100):
		lst.add(lst.size(), i)
	lst.print()

	for i in range(101, 1000, 100):
		lst.add(0, i)
	lst.print()

	print(lst.get(5))

	lst.set(5, 0)
	lst.print()

	lst.remove(5)
	lst.print()

	lst.add(5, -1)
	lst.print()
	
testLinkList()