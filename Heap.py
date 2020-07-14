import math

_DEBUG = False

def _cmp(a,b): return a-b

def _parent(index): return (index-1)//2
def _child(index, i): return index*2 + i + 1

def _valid(parent, child, cmp):
	return cmp(parent, child)<=0

def _upHeapify(heap, index, cmp):
	while(index>0):
		parentIndex = _parent(index)
		me = heap[index]
		parent = heap[parentIndex]
		if not _valid(parent, me, cmp):
			heap[index], heap[parentIndex] = heap[parentIndex], heap[index]
		# else: break
		index = parentIndex
		if _DEBUG: print(" - upHeapify: ", heap)
	return (index,0)[index < 0]

def _downHeapify(heap, index, cmp):
	if( index >= len(heap) ): return len(heap)-1
	for ch in [1,0]:
		childIndex = _child(index, ch)
		if childIndex<len(heap) and not _valid(heap[index], heap[childIndex], cmp):
			heap[index], heap[childIndex] = heap[childIndex], heap[index]
			if _DEBUG: print(" - downHeapify: ", heap)
			_downHeapify(heap, childIndex, cmp)
	return index

def heapify(heap, size, index=0, cmp=_cmp):
	if index>=size: return
	target = index

	# See if left child of root exists and is greater than root
	leftIndex = _child(index, 0)
	if leftIndex < size and not _valid(heap[index], heap[leftIndex], cmp):
		target = leftIndex

	# See if right child of root exists and is greater than root
	rightIndex = _child(index, 0)
	if rightIndex < size and not _valid(heap[index], heap[rightIndex], cmp):
		target = rightIndex

	# Change root, if needed
	if target != index:
		heap[index], heap[target] = heap[target], heap[index] # swap
		heapify(heap, size, target, cmp)


def insert(heap, item, cmp=_cmp):
	if _DEBUG: print("before raw insert: ", heap)
	heap.append(item)
	if _DEBUG: print("after raw insert: ", heap)
	_upHeapify(heap, len(heap)-1, cmp=cmp)
	if _DEBUG: print("after upHeapify insert: ", heap)

def delete(heap, index=0, cmp=_cmp):
	if _DEBUG: print("before raw delete: ", heap)
	res = heap.pop(index)
	if len(heap) <= index: return res
	heap.insert(index, heap.pop())
	if _DEBUG: print("after raw delete: ", heap)
	_downHeapify(heap, index, cmp=cmp)
	# _upHeapify(heap, index, cmp=cmp)
	#heapify(heap, len(heap), index, cmp)
	if _DEBUG: print("after downHeapify delete: ", heap)
	return res

def update(heap, index, value, cmp=_cmp):
	heap[index] = value
	_downHeapify(heap, index, cmp=cmp)
	_upHeapify(heap, index, cmp=cmp)
	return

def isHeap(heap, cmp=_cmp):
	for index in range(len(heap)):
		me = 	heap[index]
		for ch in range(2):
			childIndex = _child(index, ch)
			if childIndex>=len(heap): break
			child = heap[childIndex]
			if not _valid(me, child, cmp):
				return index
	return True

if __name__ == "__main__":
	import random
	data = [int(random.random()*100) for _ in range(10)]
	print(data)

	heap = []
	for it in data:
		insert(heap, it)
		print(heap)
		print(isHeap(heap))

	print("=======")
	print("extract")
	print(isHeap(heap))
	print(delete(heap))
	print(heap)
	print(isHeap(heap))
	print()

	print("============")
	print("extract at 3")
	print(isHeap(heap))
	print(delete(heap, 3))
	print(heap)
	print(isHeap(heap))
	print()

