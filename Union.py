
def unionFind(parents, u1, pathComp = False):
	parent = parents[u1]
	if u1 == parent: return parent

	parent = unionFind(parents, parent, pathComp)
	if pathComp: parents[u1] = parent

	return parent

# normal: O(n)
# pathComp: teta(1)
def unionBySize(parents, sizes, u1, u2, pathComp = False):
	r1 = unionFind(parents, u1, pathComp)
	r2 = unionFind(parents, u2, pathComp)
	if sizes[r1] < sizes[r2]:
		r1, r2 = r2, r1
	parents[r2] = r1
	sizes[r1] += sizes[r2]
