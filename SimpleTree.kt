package tree.simple

class SimpleTree(
	val value: String = "",
	val children: MutableList<SimpleTree>
) : List<SimpleTree> by children {
	constructor(value: String = "", vararg children: SimpleTree)
		: this(value, mutableListOf(*children))


	fun write(
		buffer: StringBuffer = StringBuffer(),
		prefix: String = "",
		childrenPrefix: String = ""
	): StringBuffer {
		buffer.append(prefix)
		buffer.append(value)
		buffer.append("\n")

		fun writeChild(child: SimpleTree?, hasNext: Boolean, childrenPrefix: String): StringBuffer {
			val pref = childrenPrefix + if (hasNext) "├─── " else "└─── "
			return if (child != null) {
				val childPref = childrenPrefix + if (hasNext) "│    " else "     "
				child.write(buffer, pref, childPref)
			} else {
				buffer.append(pref)
				buffer.append("X")
				buffer.append('\n')
				buffer
			}
		}

		//children.drop(1).asReversed().forEach {
		//	writeChild(it, true, childrenPrefix)
		//}
		//if (children.isNotEmpty())
		//	writeChild(children.first(), false, childrenPrefix)

		children.dropLast(1).forEach {
			writeChild(it, true, childrenPrefix)
		}
		if (children.isNotEmpty())
			writeChild(children.last(), false, childrenPrefix)

		return buffer
	}

	override fun toString() =
		write().toString()
}

fun SimpleTree?.preOrder(action: (SimpleTree) -> Unit) {
	if (this == null) return
	action(this)
	children.forEach { it.preOrder(action) }
}

fun SimpleTree?.inOrder(action: (SimpleTree) -> Unit) {
	if (this == null) return
	children.firstOrNull().inOrder(action)
	action(this)
	children.drop(1).forEach { it.inOrder(action) }
}

fun SimpleTree?.postOrder(action: (SimpleTree) -> Unit) {
	if (this == null) return
	children.forEach { it.postOrder(action) }
	action(this)
}


fun main() {
	val root = SimpleTree(
		"R",
		SimpleTree("a", SimpleTree("a.i"), SimpleTree("a.ii"), SimpleTree("a.iii")),
		SimpleTree("b", SimpleTree("b.1"), SimpleTree("b.2")),
		SimpleTree("c"),
		SimpleTree("d")
	)
	print(root)
}
