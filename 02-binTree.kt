package tree.bin

fun main() {
	val root = binaryTree("ROOT") {
		left("A")
		right("B") {
			left("x")
			right("y")
		}
	}.print()

	binaryTree("a") {
		bstInsert("b")
		bstInsert("a")
		bstInsert("d")
		bstInsert("c")
	}.print()
}
