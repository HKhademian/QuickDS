
def _merge(left, right, cmp):
	res = []
	leftI , rightI = 0, 0
	while leftI<len(left) and rightI<len(right):
		if cmp(left[leftI], right[rightI])<=0:
			res.append(left[leftI])
			leftI += 1
		else:
			res.append(right[rightI])
			rightI += 1

	while leftI<len(left):
		res.append(left[leftI])
		leftI += 1

	while rightI<len(right):
		res.append(right[rightI])
		rightI += 1

	return res

def _merge2(left, right, cmp):
	result = []
	while len(left)>0 or len(right)>0:
		if cmp(left[0],right[0])<=0:
			result.append(left.pop(0))
		else:
			result.append(right.pop(0))
	while len(left)>0:
		result.append(left.pop(0))
	while len(right)>0:
		result.append(right.pop(0))

	return result

def mergeSort(items, cmp = None):
	cmp = cmp if cmp != None else (lambda a,b: a-b)
	n = len(items)
	if n<=1: return items
	left = mergeSort(items[:int(n/2)],cmp)
	right = mergeSort(items[int(n/2):],cmp)
	res = _merge(left, right, cmp)
	return res

if __name__ == "__main__":
	pass
