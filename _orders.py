# I wrote this to help verify my answer in q1.1

def MakePostOrder(inorder, preorder, N):
	postOrder = []

	if preorder[0] in inorder:
		root = inorder.index(preorder[0])

	if root > 0: # left subtree
		postOrder += MakePostOrder(inorder[:root], preorder[1:root + 1], len(inorder[:root]))

	if root < N-1: # right subtree
		postOrder += MakePostOrder(inorder[root + 1:], preorder[root + 1:], len(inorder[root + 1:]))

	postOrder += [preorder[0]]

	# global i
	# i += 1
	# print(i, N, inorder, preorder, postOrder)

	return postOrder

# # Fills preorder traversal of tree with given inorder and postorder traversals in a stack
# def fillPre(inorder, postorder, int inStrt, int inEnd, stack = []):
# 	if inStrt > inEnd: return

# 	# Find index of next item inorder postorder traversal inorder, inorder.
# 	val = postorder[postIndex]
# 	inIndex = inorder.index(val)
# 	postIndex -= 1

# 	# traverse right tree
# 	fillPre(inorder, postorder, inIndex + 1, inEnd, stack)

# 	# traverse left tree
# 	fillPre(inorder, postorder, inStrt, inIndex - 1, stack)

# 	stack.append(val)

# 	return stack


i = 0
# inorder = ['G','C','B','H','D','A','F','R','E']
# preorder = ['A','B','C','G','D','H','E','F','R']
# postorder = MakePostOrder(inorder, preorder, len(inorder))
# print(postorder)

preorder = list("abcdefgh")
inorder = list("cbdfaehg")
postorder = MakePostOrder(inorder, preorder, len(inorder))
print(postoder)