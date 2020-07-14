package tree.bin.avl

import tree.bin.*

// define methods to insert/delete binary tree in avl from

val BinaryTree.avlK
	get() = this.tag as? Int ?: 0

///
fun BinaryTree.avlInsert(newNode: BinaryTree, init: BinaryTree.() -> Unit = {}) {

}

///
fun BinaryTree.avlDelete(node: BinaryTree, init: BinaryTree.() -> Unit = {}) {

}
