from typing import List

# in DS class way
def countingSort(keys:List, inplace: bool = False):
	a,b=keys[0],keys[0]

	for key in keys:
		if key<a: a=key
		if key>b: b=key
	k = b - a + 1
	print("a,b,k", a,b,k)

	# counts
	c = [0]*k
	for key in keys:
		c[key] += 1
	print("count", c)

	# commulative sum
	for i in range(1, len(c)):
		c[i] += c[i-1]
	if inplace: c.insert(0, 0)
	print("cum.sum", c)

	res = [0]*k
	if inplace:
		for key in keys:
			index = c[key]
			c[key] = index+1
			res[index] = key
	else:
		for key in keys:
			index = c[key] -1
			c[key] = index
			res[index] = key

	return res

data = [1,4,2,3,2,7,0,3]
print(countingSort(data))
print(countingSort(data, inplace= True))
