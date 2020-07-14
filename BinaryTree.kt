package tree.bin

class BinaryTree(
	var value: String = "",
	var parent: BinaryTree? = null,
	var left: BinaryTree? = null,
	var right: BinaryTree? = null,
	var tag: Any? = null, //use in AVL and RB
	init: BinaryTree.() -> Unit = {}
) {
	init {
		left?.parent = this
		right?.parent = this
		init()
	}

	override fun toString() =
		write().toString()
}

/// create bintree and insert it
fun BinaryTree.print() =
	print(this)

val BinaryTree.hasParent get() = parent != null
val BinaryTree.hasLeft get() = left != null
val BinaryTree.hasRight get() = right != null
val BinaryTree.hasChild get() = hasLeft or hasRight

val BinaryTree.isLeaf get() = !hasChild
val BinaryTree.isRoot get() = !hasParent
val BinaryTree.isLeft get() = this == parent?.left
val BinaryTree.isRight get() = this == parent?.right

val BinaryTree.grand get() = parent?.parent
val BinaryTree.uncle get() = parent?.sibling
val BinaryTree.sibling get() = if (isLeft) parent!!.right else if (isRight) parent!!.right else null

/// get bintree min valuable element before
/// sorted: { [target] ... this ... }
val BinaryTree.min
	get():BinaryTree {
		var node = this
		while (node.hasLeft) node = node.left!!
		return node
	}

/// get bintree max valuable element after
/// sorted: { a b c ... this ... [target] }
val BinaryTree.max
	get():BinaryTree {
		var node = this
		while (node.hasRight) node = node.right!!
		return node
	}

/// get bintree least valuable element after
/// sorted: { a b c ... this [target] ... }
val BinaryTree.successor
	get():BinaryTree {
		if (hasRight) return right!!.min
		var node = this // not this.parent
		while (node.isRight) node = node.parent!!
		return node.parent ?: node
	}

/// get bintree most valuable element before
/// sorted: { a b c ... [target] this ... }
val BinaryTree.proccessor
	get():BinaryTree {
		if (hasLeft) return right!!.max
		var node = this // not this.parent
		while (node.isLeft) node = node.parent!!
		return node.parent ?: node
	}

/// pretty write bintree in buffer
fun BinaryTree.write(
	buffer: StringBuffer = StringBuffer(),
	prefix: String = "",
	childrenPrefix: String = ""
): StringBuffer {
	buffer.append(prefix)
	buffer.append(value)
	buffer.append("\n")

	fun writeChild(child: BinaryTree?, hasNext: Boolean, childrenPrefix: String): StringBuffer {
		val pref = childrenPrefix + if (hasNext) "├─── " else "└─── "
		return if (child != null) {
			val childPref = childrenPrefix + if (hasNext) "│    " else "     "
			child.write(buffer, pref, childPref)
		} else {
			buffer.append(pref)
			buffer.append("{null}")
			buffer.append('\n')
			buffer
		}
	}

	if (hasChild) {
		// //first left
		//writeChild(this.left, hasRight, childrenPrefix)
		//writeChild(this.right, false, childrenPrefix)

		// first right
		writeChild(this.right, hasLeft, childrenPrefix)
		writeChild(this.left, false, childrenPrefix)
	}

	return buffer
}

/// rotate bintree to left
fun BinaryTree.rotateLeft() {
	//if(BST.DEBUG) console.log("RotateLeft("+this.key+")")

	val other = this.right ?: return
	val alpha = this.left
	val beta = other.left
	val gama = other.right

	this.right = beta
	beta?.parent = this

	other.parent = this.parent
	if (!this.hasParent) {
		this.parent = other
	} else if (this.isLeft) {
		this.parent!!.left = other
	} else if (this.isRight) {
		this.parent!!.right = other
	}
	other.left = this
	this.parent = other
}

/// rotate bintree to right
fun BinaryTree.rotateRight() {
	// if(BST.DEBUG) console.log("RotateRight("+this.key+")")

	val other = this.left ?: return
	val alpha = other.left
	val beta = other.right
	val gama = this.right

	this.left = beta;
	beta?.parent = this

	other.parent = this.parent
	if (!this.hasParent) {
		this.parent = other
	} else if (this.isLeft) {
		this.parent!!.left = other
	} else if (this.isRight) {
		this.parent!!.right = other
	}
	other.right = this
	this.parent = other
}

/// visit bintree PreOrder
fun BinaryTree?.preOrder(action: (BinaryTree) -> Unit) {
	if (this == null) return
	action(this)
	left.preOrder(action)
	right.preOrder(action)
}

/// visit bintree inOrder
fun BinaryTree?.inOrder(action: (BinaryTree) -> Unit) {
	if (this == null) return
	left.preOrder(action)
	action(this)
	right.preOrder(action)
}

/// visit bintree PostOrder
fun BinaryTree?.postOrder(action: (BinaryTree) -> Unit) {
	if (this == null) return
	action(this)
	left.preOrder(action)
	right.preOrder(action)
}

/// create bintree as root node
fun binaryTree(value: String = "", init: BinaryTree.() -> Unit = {}) =
	BinaryTree(value).also { it.init() }

/// create bintree as left node of current bintree
/// better to use insert instead
fun BinaryTree.left(value: String = "", init: BinaryTree.() -> Unit = {}) =
	BinaryTree(value, this, init = init).also { this.left = it; }

/// create bintree as right node of current bintree
/// better to use insert instead
fun BinaryTree.right(value: String = "", init: BinaryTree.() -> Unit = {}) =
	BinaryTree(value, this, init = init).also { this.right = it; }


/// insert new node
fun BinaryTree.bstInsert(newNode: BinaryTree, init: BinaryTree.() -> Unit = {}): BinaryTree {
	val cmp = { a: BinaryTree?, b: BinaryTree? ->
		when {
			a == null -> (if (b == null) 0 else -1)
			b == null -> 1
			else -> a.value.compareTo(b.value)
		}
	}
	val left = this.left
	val right = this.right
	if (cmp(this, newNode) > 0) {
		if (right == null) {
			this.right = newNode
			newNode.parent = this
		} else {
			right.bstInsert(newNode)
		}
	} else {
		if (left == null) {
			this.left = newNode
			newNode.parent = this
		} else {
			left.bstInsert(newNode)
		}
	}
	return newNode.also(init)
}

/// create bintree and insert it
fun BinaryTree.bstInsert(value: String = "", init: BinaryTree.() -> Unit = {}) =
	bstInsert(BinaryTree(value, this), init)
