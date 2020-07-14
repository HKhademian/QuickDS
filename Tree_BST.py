_DEBUG = True

class BST():
	def __init__(self, key, parent=None):
		self.key		:any = key
		self.parent	:BST = parent
		self.left		:BST = None
		self.right	:BST = None

	def isLeft(self): return self.parent and self.parent.left == self
	def isRight(self): return self.parent and self.parent.right == self
	def hasParent(self): return not not self.parent
	def hasLeft(self): return not not self.left
	def hasRight(self): return not not self.right
	def hasChild(self): return self.hasLeft() or self.hasRight()
	def isLeaf(self): return not self.hasChild()
	def isRoot(self):  return not self.hasParent()

	def getRoot(self): return self.parent.getRoot() if self.hasParent() else self
	def getGrandParent(self) : return self.parent.parent if self.hasParent() else None
	def getUncle(self): return self.parent.getSibling() if self.hasParent() else None
	def getSibling(self): return self.parent.left if self.isRight() else self.parent.right if self.isLeft() else None

	def getText(self):
		return f"{self.key}"

	def getMin(self):
		cur = self
		while cur.hasLeft(): cur = cur.left
		return cur

	def getMax(self):
		cur = self
		while cur.hasRight(): cur = cur.right
		return cur

	def getSuccessor(self):
		if self.hasRight(): return self.right.getMin()
		cur = self # not self.parent
		while cur.isRight(): cur = cur.parent
		return cur.parent if cur.hasParent() else cur

	def getPreccessor(self):
		if self.hasLeft(): return self.left.getMax()
		cur = self # not self.parent
		while cur.isLeft(): cur = cur.parent
		return cur.parent if cur.hasParent() else cur

	def rotateLeft(self):
		if _DEBUG: print(f"RotateLeft({self.key})")

		other = self.right
		if not other: return
		alpha = self.left
		beta = other.left
		gama = other.right

		self.right = beta
		if beta: beta.parent = self

		other.parent = self.parent
		if self.isLeft():
			self.parent.left = other
		elif self.isRight():
			self.parent.right = other
		self.parent = other
		other.left = self

	def rotateRight(self):
		if _DEBUG: print(f"RotateRight({self.key})")

		other = self.left
		if not other: return
		alpha = other.left
		beta = other.right
		gama = self.right

		self.left = beta
		if beta: beta.parent = self

		other.parent = self.parent
		if self.isLeft():
			self.parent.left = other
		elif self.isRight():
			self.parent.right = other
		self.parent = other
		other.right = self


	def write(self, buffer = [], prefix = "", childrenPrefix=""):
		buffer.append(f"{prefix}{self.getText()}\n")

		def writeChild(self, child, hasNext, buffer, childrenPrefix):
			pref = childrenPrefix + ("├─── " if hasNext else "└─── ")
			if child:
				childPref = childrenPrefix + ("│    " if hasNext else "     ")
				return child.write(buffer, pref, childPref)
			else:
				buffer.append(f"{pref}[NONE]\n")
				return buffer

		if self.hasChild():
			#  first show right for better visiuals
			buffer = writeChild(self, self.right, True, buffer, childrenPrefix)
			buffer = writeChild(self, self.left, False, buffer, childrenPrefix)

		return buffer

	def print(self):
		return print("".join(self.write([])))

	def preOrder(self, visit = (lambda a:None)):
		visit(self)
		if self.hasLeft(): self.left.preOrder( visit )
		if self.hasRight(): self.right.preOrder( visit )

	def inOrder(self, visit = (lambda a:None)):
		if self.hasLeft(): self.left.postOrder( visit )
		visit( self )
		if self.hasRight(): self.right.postOrder( visit )

	def postOrder(self, visit = (lambda a:None)):
		if self.hasLeft(): self.left.postOrder( visit )
		if self.hasRight(): self.right.postOrder( visit )
		visit( self )

	# to support avl,rb augmention
	def newNode(self, key):
		return BST(key)

	# create new node from key, add it to bst and return it
	def insert(self, key):
		node = self.newNode(key)
		return self.insertNode(node)

	# insert node to bst-style parent
	def insertNode(self, node) :
		if not node: return None

		if node.key > self.key:
			if self.hasRight():
				return self.right.insertNode(node)
			else:
				node.parent = self
				self.right = node
		else:
			if self.hasLeft():
				return self.left.insertNode(node)
			else:
				node.parent = self
				self.left = node

		return node

	def delete(self):
		print(f"delete {self.key}")
		repl = None
		if not self.hasLeft():
			repl = self.right
		elif not self.hasRight():
			repl = self.left
		else:
			repl = self.getSuccessor()
			self.key = repl.key
			return repl.delete()

		if repl: repl.parent = self.parent
		if self.isLeft(): self.parent.left = repl
		elif self.isRight(): self.parent.right = repl
		else: 1/0

		return self.getRoot()

# if __name__ == "__main__":
# 	# data = [10, 5, 6, 2, 6, 4, 7, 8, 9, 1, 2, 5]
# 	import random
# 	data = [int(random.random()*100) for _ in range(10)]
# 	tree = BST(data.pop(0))
# 	X = 1
# 	for it in data:
# 		#print(f"---{X}--- add({it}):")
# 		X+=1
# 		tree.insert(it)
# 		tree = tree.getRoot()
# 		#tree.print()
# 		pass
#
# 	tree = tree.getRoot()
# 	tree.print()
#
# 	tree = tree.delete()
# 	tree.print()
#
# 	#tree.rotateLeft()
# 	#tree = tree.getRoot()
# 	#tree.print()
#
# 	#tree.rotateRight()
# 	#tree = tree.getRoot()
# 	#tree.print()
#
# 	pass

if __name__ == "__main__":
	pass

	# after final exam I check my answer to testify my response
	# I also relized the beauty of my kotlin dsl

	tree = BST(10)

	tree.left = BST(1, tree)
	tree.left.right = BST(5, tree.left)
	tree.left.right.left = BST(3, tree.left.right)
	tree.left.right.right = BST(8, tree.left.right)
	tree.right = BST(15, tree)
	tree.right.left = BST(12, tree.right)
	tree.right.right = BST(25, tree.right)
	tree.right.right.left = BST(21, tree.right.right)
	tree.right.right.left.right = BST(23, tree.right.right.left)
	tree.right.right.right = BST(30, tree.right.right)

	tree.print()

	#tree.right.delete()
	#tree.print()

	tree.rotateLeft()
	tree.print()


