from HW04Q06 import *

def _main():
	infix = input("Enter your phrase: ")
	# variables = eval(input("Enter variables as map [ {'a':2,'b':3} ]: "))
	variables = {}
	postfix = infixToPostfix(infix)
	tree = postfixToTree(postfix)
	value = tree.eval(variables)
	print ("Expression value is = ", value)

if __name__ == "__main__":
	_main()
