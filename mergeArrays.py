from typing import List
import math
from Heap import insert as insertHeap
from Heap import delete as extractHeap

_DEBUG = False

def _cmp(parent, child):
	return parent[0] - child[0]

# O(k*lgn) => worst (k=n) => like heapsort
def mergeArrays(lists:List[List]):
	heap = []
	res = []

	for listIndex in range(len(lists)):
		lst = lists[listIndex]
		itemIndex = 0
		if len(lst)>0: insertHeap(heap, (lst[itemIndex], itemIndex, listIndex), cmp=_cmp)

	if _DEBUG: print("heap", heap)

	while len(heap)>0:
		(value, itemIndex, listIndex) = extractHeap(heap, cmp=_cmp)
		if _DEBUG: print("item", (value, itemIndex, listIndex))
		res.append(value)
		lst = lists[listIndex]
		itemIndex += 1
		if itemIndex<len(lst):
			insertHeap(heap, (lst[itemIndex], itemIndex, listIndex), cmp=_cmp)

	return res

if __name__ == "__main__":
	list1 = list(range(-1,100,17))
	list2 = list(range(2,100,23))
	list3 = list(range(1,100,13))
	print("list1",list1)
	print("list2",list2)
	print("list3",list3)
	cum = mergeArrays([list1, list2, list3])
	print(cum)
