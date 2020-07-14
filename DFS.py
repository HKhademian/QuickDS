MAX = 1000

def BFS1(visits, adjs, x):
	queue = []
	queue.append(x)
	while len(queue):
		cur = queue.pop(0)
		adj = adjs[cur]
		if not visits[cur]:
			visits[cur] = True
			# process
			for it in adj:
				queue.append(it)

def DFS(visits, adjs, x):
	queue = []
	queue.append(x)
	while len(queue):
		cur = queue.pop(-1)
		adj = adjs[cur]
		if not visits[cur]:
			visits[cur] = True
			# process
			for it in adj:
				queue.append(it)

if __name__ == "__main__":
	visit = [False] * MAX
	adj = [[]] * MAX
	# for i in 10
