package tree.bin.eq

import tree.bin.*

fun main() {
	val root = binaryTree("ROOT") {
		simpleInsert("a")
		simpleInsert("b")
		simpleInsert("c")
		simpleInsert("d")
		simpleInsert("e") {
			simpleInsert("w")
			simpleInsert("x")
			simpleInsert("y")
			simpleInsert("z")
		}
	}
	print(root)
}
