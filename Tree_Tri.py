class Tri():
	def __init__(self, ch: chr=None, parent=None):
		self.ch			:chr = ch
		self.parent	:Tri = parent
		self.exists	:bool = False
		self.children     = {}
		if parent:
			parent.children[ch] = self

	def __str__(self):
		if not self.parent: return str(self.ch) if self.ch else ""
		return str(self.parent) + self.ch

	def getRoot(self):
		return self.parent.getRoot() if self.parent else self

	def getChild(self, key):
		key = key.lower()
		return self.children.get(key) or Tri(key, self)

	def add_rec(self, text: str):
		if not text or not len(text):
			self.exists = True
			return
		key = text[0]
		node = self.getChild(key)
		return node.add_rec(text[1:])

	def add_loop(self, text: str):
		node = self #.getRoot()
		for ch in text:
			node = node.getChild(ch)
		node.exists = True

	def add(self, text:str):
		return self.add_loop(text)

	def toList(self, buffer=[]):
		if self.exists:
			buffer.append(str(self))
		for ch in self.children:
			self.children[ch].toList(buffer)
		return buffer

	def find(self, text:str):
		node = self
		for ch in text:
			if not ch in node.children: return False
			node = node.children[ch]
		return node

	def delete(self, text: str):
		node = self.find(text)
		if node and node.exists:
			node.exists = False
			return True
		return False

def LCP(node: Tri):
	while len(node.children)==1:
		ch = next(iter(node.children))
		node = node.children[ch]
	return node # this is deepest common node

# if __name__ == "__main__":
# 	// const dict  = new Tri("Hossain", "Hassan", "Hamid");
# 	// const dict  = new Tri("Book", "Booklet", "Boom", "Bombs");
# 	// const dict  = new Tri("Admiral", "Book", "Booklet", "Boom","Bombs");
# 	const dict  = new Tri("Compact", "Companionate", "Complex", "Compare", "Compass");
# 	const lcp = dict.LCP();
# 	const res = lcp.toString();
# 	console.log("LCP:", res);


if __name__ == "__main__":
	# ["Hossain", "Hassan", "Hamid"]
	# ["Book", "Booklet", "Boom", "Bombs"]
	# ["Admiral", "Book", "Booklet", "Boom","Bombs"]
	tri = Tri()
	for text in ["Compact", "Companionate", "Complex", "Compare", "Compass"]:
		tri.add(text)

	print(tri.toList())

	lcp = LCP(tri)
	print(lcp)

