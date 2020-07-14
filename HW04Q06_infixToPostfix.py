OP = "+-*/"

class Node:
	def __init__(self, c, left = None, right = None):
		self.c = c
		self.left = left
		self.right = right
	
	def eval(self, mem = {}):
		c = self.c
		l = self.left.eval(mem) if self.left else 0
		r = self.right.eval(mem) if self.right else 0
		if c == '+':
			return l + r
		elif c == '-':
			return l - r
		elif c == '*':
			return l * r
		elif c == '/':
			return l / r
		elif not ('0' <= c <= '9'):
			return mem[c]
		else:
			return int(c)
	
	def print(self, ln=True):
		if self.c in OP:
			print ("(", end="")
			self.left.print(False)
			print (self.c, end="")
			self.right.print(False)
			print (")", end="")
		else:
			print (self.c, end="")
		if ln: print()

# used in q2 ( also use parantesis as possible, it doesnt check priorities )
def infixToPostfix(expression):
	output = []
	stack = []

	for c in expression:
		if c == '(' or c in OP:
			stack.append(c)
		elif c == ')':
			while len(stack)>0:
				tops = stack.pop()
				if tops == '(': break
				output.append(tops)
		else:
			output.append(c)

	while len(stack)>0: output.append(stack.pop())

	return "".join(output)

def postfixToTree(expression):
	stack = []
	for c in expression:
		node = Node(c)
		if c in OP:
			node.right = stack.pop()
			node.left = stack.pop()
		stack.append(node)
	return stack.pop()

def infixToTree(expression):
	postfix = infixToPostfix(expression)
	return postfixToTree(postfix)

# test
def _test():
	infix = input("Enter your phrase: ")
	postfix = infixToPostfix(infix)
	print(postfix)
	tree = postfixToTree(postfix)
	tree.print(False )
	value = tree.eval()
	print(" = ", value)

if __name__ == "__main__":
	_test()
