class Graph(object):
	def __init__(self, directed=False):
		self.adj_list = {}
		self.directed = directed

	def __str__(self):
		return str(self.adj_list)

	def add_node(self, node):
		if node not in self.adj_list:
			self.adj_list[node] = []
		else:
			print(f"Node '{node}' is already in the adj_list -- returning")

	def add_edge(self, node1, node2):
		if node1 in self.adj_list and node2 in self.adj_list:
			self.adj_list[node1].append(node2)
			if not self.directed:
				self.adj_list[node2].append(node1)

	def hasPathBFS(self, start_node, dest):
		visited = set()
		mqueue = []

		if start_node not in self.adj_list or dest not in self.adj_list:
			return False

		mqueue.insert(0, start_node)
		visited.add(start_node)

		while len(mqueue) > 0:
			mq = mqueue.pop()

			if mq == dest:
				return True

			for neigh in self.adj_list[mq]:
				if neigh not in visited:
					mqueue.insert(0, neigh)
					visited.add(neigh)

		return False

	def shortest_path_bfs(self, start_node, end_node):
		mqueue = []
		path = []
		visited = set()

		if start_node not in self.adjList:
			return

		mqueue.insert(0, [start_node, 0])
		visited.add(start_node)

		while len(mqueue) > 0:
			itm = mqueue.pop()
			i,j = itm[0],itm[1]

			print(f"Visited '{i}' -- {j}")
			path.append(itm)

			if i == end_node:
				print(f"Found end node '{end_node}'")
				return j

			for n in self.adjList[i]:
				if n not in visited:
					visited.add(n)
					mqueue.insert(0, [n,j+1])

		return -1

	def DFS(self, mitem, visited, dest):
		visited.add(mitem)

		if mitem == dest:
			return True

		for neigh in self.adj_list[mitem]:
			if neigh not in visited:
				if self.DFS(neigh, visited, dest):
					return True

		return False

	def hasPathDFS(self, start_node, dest):		
		return self.DFS(start_node, set(), dest)
