def gcd(a,b):
	return a if b==0 else gcd(b, a % b)

def gcd2(a,b):
	while b!=0: a,b = b,a%b
	return a


def fact(n):
	return 1 if n<2 else n * fact(n-1)

def factorial(n):
	if n <2: return 1
	res = 1
	for i in range(2, n + 1): res *= i
	return res


def fib(n):
	return 1 if n<=2 else fib(n-1) + fib(n-2)

def finonachi(n):
	a,b = 1,1
	for i in range(3,n+1): a,b = b, a + b
	return b


def strrev(str):
	return str if not str or len(str)<=1 else str[-1] + strrev(str[0:-1])
