package tree.bin.eq

import tree.bin.*

// in this method, we encode a normal tree in a binary tree

var BinaryTree.simpleFirstChild: BinaryTree?
	get() = this.left
	set(value) {
		this.left = value
	}

var BinaryTree.simpleSiblingNext: BinaryTree?
	get() = this.right
	set(value) {
		this.left = value
	}

val BinaryTree.simpleSiblingBefore: BinaryTree?
	get() = if (this.isRight) this.parent else null

val BinaryTree.simpleParent: BinaryTree?
	get() = this.simpleSiblingBefore?.simpleParent ?: this.parent

fun BinaryTree.simpleInsert(newNode: BinaryTree, init: BinaryTree.() -> Unit = {}): BinaryTree {
	val left = this.left
	if (left == null) {
		this.left = newNode
		newNode.parent = this
	} else {
		var cur = this
		while (cur.simpleSiblingNext != null)
			cur = cur.simpleSiblingNext!!
		cur.right = newNode
		newNode.parent = cur
	}
	newNode.init()
	return newNode
}

fun BinaryTree.simpleInsert(value: String, init: BinaryTree.() -> Unit = {}) =
	simpleInsert(BinaryTree(value)).also(init)

