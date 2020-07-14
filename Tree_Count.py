from Tree_AVL import AVLTree

def _getCounting(node):
	return node.count if node else 0

def _updateCounting(node):
	if not node: return 0
	node.count = _updateCounting(node.left) + _updateCounting(node.right) + 1
	return node.count

class CountingAVLTree(AVLTree):
	def __init__(self, key):
		super().__init__(key)
		self.count = 1

	def getText(self):
		return f"<{self.count}> {self.key}"

	def newNode(self, key):
		return CountingAVLTree(key)

	def getNode(self, index):
		countLeft = _getCounting(self.left)
		if index < countLeft: return self.left.getNode(index)
		if index == countLeft: return self
		if not self.hasRight(): return None
		return self.right.getNode(index - countLeft -1)

	def rotateLeft(self):
		super().rotateLeft()
		_updateCounting(self.parent or self)

	def rotateRight(self):
		super().rotateRight()
		_updateCounting(self.parent or self)

	def insertNode(self, node):
		node = super().insertNode(node)
		_updateCounting(self.parent or self)
		return node

	def delete(self):
		node = super().delete()
		_updateCounting(self.parent or self)
		return node


if __name__ == "__main__":
	pass
	# data = [10, 5, 6, 2, 6, 4, 7, 8, 9, 1, 2, 5]
	import random
	data = [int(random.random()*100) for _ in range(10)]
	tree = CountingAVLTree(data.pop(0))
	X = 1
	for it in data:
		print(f"---{X}--- add({it}):")
		X+=1
		tree.insert(it)
		tree = tree.getRoot()
		#tree.print()
		pass

	tree = tree.getRoot()
	tree.print()

	tree.rotateLeft()
	tree = tree.getRoot()
	tree.print()

	tree.rotateRight()
	tree = tree.getRoot()
	tree.print()

	tree = tree.delete()
	tree.print()

	print(tree.getNode(0).key)
	print(tree.getNode(1).key)
	print(tree.getNode(2).key)
	print(tree.getNode(3).key)
	print(tree.getNode(4).key)
	print(tree.getNode(5).key)
	print(tree.getNode(6).key)
	print(tree.getNode(7).key)
	print(tree.getNode(8).key)
	print(tree.getNode(9).key)
	print(tree.getNode(10).key)
	print(tree.getNode(45).key)
	print(tree.getNode(100))


	pass
