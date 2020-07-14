#MST

# m*lgm
def _sortEdges(edges):
	from SortMerge import mergeSort
	cmp = lambda a,b: a[0]-b[0]
	res = mergeSort(edges, cmp)
	return res

def _vertecies(edges):
	verts = []
	for edge in edges:
		if not edge[1] in verts: verts.append(edge[1])
		if not edge[2] in verts: verts.append(edge[2])
	return verts

# n^2
### u2->u1
def _unionSimple(unions, u1, u2):
	for i in range(len(unions)):
		if unions[i] == u2:
			unions[i] = u1


# #lgn
# ### u1->ux and u2->ux , where ux is larger union
# ### u = (index, size, next)
# def _unionLinked(unions, unionLinks, u1, u2):
# 	union1, union2 = unions[u1], unions[u2]
# 	if union1[1]<union2[1]: u1, u2, union1, union2 = u2, u1, union2, union1
# 	unions[u1] = (u)

# 	while cur!=None:
# 		curU
# 		unions[cur] = u1
# 		next = cur[3]


def _unionSized(unionParents, unionSizes, u1, u2):
	from Union import unionBySize
	unionBySize(unionParents, unionSizes, u1, u2, )


def kruskal(edges):
	# final edges to walk in tree
	res = []
	# extract vertecies from edge map
	verts = _vertecies(edges)

	# # each vert is in a unique union, use simple union
	# unions = [i for i in range(len(verts))]

	# # each vert is in a unique union, use linked union
	#unions = [(i, 1, None) for i in range(len(verts))]

	# union
	unions = [i for i in range(len(verts))]
	unionSizes = [1 for union in unions]

	# sort edges depend on edge cost
	edges = _sortEdges(edges)

	for edge in edges:
		_, v1, v2 = edge

		# sorted vertex names
		if v2 < v1: v1, v2 = v2, v1

		i1, i2 = verts.index(v1), verts.index(v2)
		u1, u2 = unions[i1], unions[i2]

		# prevent loops
		if u1==u2: continue

		# we can use this edge
		res.append(edge)
		_unionSized(unions, unionSizes, u1, u2)

	return res

if __name__ == "__main__":
	edges = [ \
		( 7, 'A', 'B'), \
		( 5, 'A', 'D'), \
		( 9, 'B', 'D'), \
		( 8, 'B', 'C'), \
		( 7, 'B', 'E'), \
		( 5, 'C', 'E'), \
		( 15, 'D', 'E'), \
		( 6, 'D', 'F'), \
		( 8, 'E', 'F'), \
		( 9, 'E', 'G'), \
	]
	print(edges)

	res = kruskal(edges)
	cost = 0
	for edge in res: cost += edge[0]
	print(cost, res)


