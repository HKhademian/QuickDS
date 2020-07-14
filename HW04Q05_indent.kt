class Node (
	val title: String,
	val childrens: List<Node> = emptyListOf<>(),
) {

	fun printMe(level: int = 0) {
		print("\t".repeat(level))
		print(title)
		if(childrens.isNotEmpty()) {
			print("\t".repeat(level))
			println(" (")
			childrens.forEach {
				it.printMe(level + 1)
			}
			print("\t".repeat(level))
			println(")")
		}
	}
	
}

fun main() {
	val node = Node("Sales", listOf(
		Node("Domestic"),
		Node("International", listOf(
			Node("Canada"),
			Node("S. America"),
			Node("Overseas", listOf(
				Node("Africa"),
				Node("Europe"),
				Node("Asia"),
				Node("Australia"),
			)),
		)),
	)),
	node.printMe()
}
