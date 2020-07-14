from Tree_BST import BST

_BLACK = 0
_RED = 1
_DEBUG = True

def _repairAfterInsertCase4Step2(node):
	parent = node.parent
	grandParent = parent.parent
	if node.isLeft():
		grandParent.rotateRight()
	else:
		grandParent.rotateLeft()
	grandParent.color = _RED
	parent.color = _BLACK

def _repairAfterInsertCase4(node, parent):
	if node.isRight() and parent.isLeft():
		parent.rotateLeft()
		node = node.left
	elif node.isLeft() and parent.isRight():
		parent.rotateRight()
		node = node.right
	return _repairAfterInsertCase4Step2(node)

def _repairAfterInsertCase3(node, parent, uncle):
	parent.color = _BLACK
	uncle.color = _BLACK
	grandParent = parent.parent
	grandParent.color = _RED
	return _repairAfterInsert(grandParent)

def _repairAfterInsertCase2(node):
	pass

def _repairAfterInsertCase1(node):
	node.color = _BLACK

def _repairAfterInsert(node):
	parent = node.parent
	if not parent: return _repairAfterInsertCase1(node)
	if parent.color == _BLACK: return _repairAfterInsertCase2(node)
	uncle = node.getUncle()
	if uncle and uncle.color == _RED: return _repairAfterInsertCase3(node, parent, uncle)
	return _repairAfterInsertCase4(node, parent)


class RedBlackTree(BST):
	def __init__(self, key, parent=None):
		super().__init__(key, parent)
		self.color = _BLACK

	def getText(self):
		return f"{self.color} > {self.key}"

	def newNode(self, key):
		return RedBlackTree(key)

	def insertNode(self, node):
		super().insertNode(node)
		node.color = _RED
		_repairAfterInsert(node)

	#def deleteNode(self, node):
	#	super().deleteNode(node)
	#	node.color = _RED
	#	# _repairAfterDelete(node)

if __name__ == "__main__":
	pass
	# # data = [10, 5, 6, 2, 6, 4, 7, 8, 9, 1, 2, 5]
	# import random
	# data = [int(random.random()*100) for _ in range(150)]
	# tree = RedBlackTree(data.pop(0))
	# X = 1
	# for it in data:
	# 	print(f"---{X}--- add({it}):")
	# 	X+=1
	# 	tree.insert(it)
	# 	tree = tree.getRoot()
	# 	#tree.print()
	# 	pass

	# tree = tree.getRoot()
	# tree.print()

	# #tree.rotateLeft()
	# #tree = tree.getRoot()
	# #tree.print()

	# #tree.rotateRight()
	# #tree = tree.getRoot()
	# #tree.print()

	# pass


	root = RedBlackTree(47)
	root.left = RedBlackTree(32, root)
	root.right = RedBlackTree(71, root)
	root.right.color = _RED
	root.right.left = RedBlackTree(65, root.right)
	root.right.left.left = RedBlackTree(55, root.right.left)
	root.right.left.left.color = _RED
	root.right.left.right = RedBlackTree(67, root.right.left)
	root.right.left.right.color = _RED
	root.right.right = RedBlackTree(87, root.right)
	root.print()

	root.insert(70)
	root = root.getRoot()
	root.print()


