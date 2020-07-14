def hanoi(n, start, end, temp):
	if n==1:
		print(start, '->', end)
		return 1
	x = 0
	x += hanoi(n-1, start, temp, end)
	x += hanoi(1, start, end, temp)
	x += hanoi(n-1, temp, end, start)
	return x

def hanoiXSE(n, start, end, temp):
	if n==1:
		print('XSE:', start, 'S->T', temp)
		print('XSE:', temp, 'S->T', end)
		# input()
		return 2
	x = 0
	x += hanoiXST(n-1, start, temp, end)
	x += hanoiXET(n-1, temp, end, start)
	# print('+(')
	x += hanoiXST(1, start, temp, end)
	# print(')+')
	x += hanoiXST(n-1, end, temp, start)
	x += hanoiXET(n, temp, end, start)
	return x

def hanoiXST(n, start, end, temp):
	if n==1:
		print('XST:', start, 'S->E', end)
		# input()
		return 1
	x = 0
	x += hanoiXSE(n-1, start, temp, end)
	x += hanoiXST(1, start, end, temp)
	x += hanoiXST(n-1, temp, end, start)
	return x

def hanoiXET(n, start, end, temp):
	if n==1:
		print('XET:', start, 'S->E', end)
		# input()
		return 1
	x = 0
	x += hanoiXET(n-1, start, temp, end)
	x += hanoiXET(1, start, end, temp)
	x += hanoiXSE(n-1, temp, end, start)
	return x
