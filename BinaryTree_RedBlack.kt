package tree.bin.redblack

import tree.bin.*

// define methods to insert/delete binary tree in redblack from

enum class AVL_Color { Black,Red }

val BinaryTree.rbColor
	get() = this.tag as? AVL_Color ?: AVL_Color.Black

///
fun BinaryTree.rbInsert(newNode: BinaryTree, init: BinaryTree.() -> Unit = {}) {

}

///
fun BinaryTree.rbDelete(node: BinaryTree, init: BinaryTree.() -> Unit = {}) {

}
