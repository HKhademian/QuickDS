def Hanoi(n, a='A',b='B', c='C'):
	if n==1:
		print("from {} to {}".format(a,c))
		return
	Hanoi(n-1, a,c,b)
	print("from {} to {}".format(a,c))
	Hanoi(n-1,b,a,c)

Hanoi(3)
