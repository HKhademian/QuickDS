
def CheckMe(text):
	stack = []
	# i=0
	for ch in text:
		# i+=1
		# print(i, ch, stack)
		if ch in "[{(":
			stack.append(ch)
		else:
			if len(stack)<=0:
				return False
			d = stack.pop()
			if (d=='[' and ch!=']' ) or (d=='{' and ch!='}' ) or (d=='(' and ch!=')' ):
				return False
	return len(stack)<=0

print(CheckMe(input("Enter your phrase: ")))
