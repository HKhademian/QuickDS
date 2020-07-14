from Tree_BST import BST

def _getHeight(node):
	return node.height if node else 0

def _updateBalance(node):
	if not node: return 0
	leftH = _updateBalance(node.left)
	rightH = _updateBalance(node.right)
	node.height = max(leftH, rightH) + 1
	node.balance = rightH - leftH
	return node.height

def _rebalance(node, propagate = False):
	if not node: return
	_updateBalance(node)
	while node.balance > 1 or node.balance < -1:
		if node.balance > 1:
			if node.right and node.right.balance < 0: # case 3 (right-right)
				node.right.rotateRight()
			node.rotateLeft()
		elif node.balance < -1:
			if node.left and node.left.balance > 0: # case 2 (left-left)
				node.left.rotateLeft()
			node.rotateRight()
		_updateBalance(node)
	if propagate: _rebalance(node.parent, propagate)

class AVLTree(BST):
	def __init__(self, key):
		super().__init__(key)
		self.height = 1
		self.balance = 0

	def getText(self):
		return f"<{self.balance},{self.height}> {self.key}"

	def newNode(self, key):
		return AVLTree(key)

	def rotateLeft(self):
		super().rotateLeft()
		_updateBalance(self)

	def rotateRight(self):
		super().rotateRight()
		_updateBalance(self)

	def insertNode(self, node):
		node = super().insertNode(node)
		_rebalance(self)
		return node

	def delete(self):
		node = super().delete()
		_rebalance(self, propagate=True)
		return node


if __name__ == "__main__":
	pass
	# data = [10, 5, 6, 2, 6, 4, 7, 8, 9, 1, 2, 5]
	import random
	data = [int(random.random()*100) for _ in range(100)]
	tree = AVLTree(data.pop(0))
	X = 1
	for it in data:
		print(f"---{X}--- add({it}):")
		X+=1
		tree.insert(it)
		tree = tree.getRoot()
		#tree.print()
		pass

	tree = tree.getRoot()
	_updateBalance(tree)
	tree.print()

	#tree.rotateLeft()
	#tree = tree.getRoot()
	#tree.print()

	#tree.rotateRight()
	#tree = tree.getRoot()
	#tree.print()

	tree = tree.delete()
	tree.print()


