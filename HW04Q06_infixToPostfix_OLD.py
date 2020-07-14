# this technique used in q2
# it does not support prantessiss and oprators rank and multi digit numbers
# also I don't handle error phrase (simple but useless in this question)

# prantessis-less phrase
def infixToPostfix(text):
	OP = "+-*/"
	stack = []
	output = []
	for c in text:
		if c in "+-*/":
			while len(stack)>0 and not stack[-1] in OP:
				output.append(stack.pop())
		stack.append(c)
	while len(stack)>0:
		output.append(stack.pop())
	return "".join(output)

# test
def test():
	print(infixToPostfix(input("Enter your phrase: ")))
test()
