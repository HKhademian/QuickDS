from Heap import insert as heapInsert
from Heap import delete as heapExtract

# each huffman node is tuple (0: char, 1: size, 2: left, 3: right)

def _cmp(this, that):
	# if not that: return -1
	# if not this: return 1
	return -(that[1]-this[1])

def _write(node, buffer=[], s = "") :
	if not node: return buffer
	if not node[2] and not node[3]: # leaf
		if node[0]: # only real chars
			buffer .append( f"{node[0]} : {s}\n")
		return buffer
	_write(node[2], buffer, s + "0")
	_write(node[3], buffer, s + "1")
	return buffer

def _print(node) :
	return print("".join(_write(node, [])))

def insert(huffman, char, count):
	node = [char, count, None, None]
	heapInsert(huffman, node, cmp=_cmp)
	return huffman

def decode(huffman):
	while len(huffman)>1:
		print(huffman)
		left = heapExtract(huffman, cmp=_cmp)
		right = heapExtract(huffman, cmp=_cmp)
		print("extracted", (left[0], left[1]), (right[0], right[1]))
		count = left[1] + right[1]
		root = (None, count, left, right)
		heapInsert(huffman, root, cmp=_cmp)
	return huffman.pop()

if __name__ == "__main__":
	huffman = []
	# while True:
	# 	char = str(input("Enter char to insert or empty to decode: "))
	# 	if not len(char): break
	# 	count = int(input("Enter char count:"))
	# 	insert(huffman, char[0], count)
	insert(huffman, "a", 5)
	insert(huffman, "b", 9)
	insert(huffman, "c", 12)
	insert(huffman, "d", 13)
	insert(huffman, "e", 16)
	insert(huffman, "f", 45)
	res = decode(huffman)
	_print(res)

