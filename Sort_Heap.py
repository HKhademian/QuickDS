from Heap import heapify

def heapSort(data):
	n = len(data)

	for i in range(n//2 - 1, -1, -1):
		heapify(data, n, i)

	for i in range(n-1, 0, -1):
		data[i], data[0] = data[0], data[i] # swap
		heapify(data, i, 0)
