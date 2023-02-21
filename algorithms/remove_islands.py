class Node:
	def __init__(self, x, y, value):
		self.x = x
		self.y = y
		self.value = value
		self.neighbors = set()

def is_edge_node(node, graph_size):
	xv = node.x == 0 or node.x == graph_size-1
	yv = node.y == 0 or node.y == graph_size-1

	return xv or yv

def dfs_help(graph, node, visited):
	visited.add(node)

	for n in node.neighbors:
		neigh = graph[n[0]][n[1]]
		
		# Visit the next neighbor
		if neigh not in visited and neigh.value == "#":
			dfs_help(graph, neigh, visited)

def dfs(graph, graph_size, start_node, visited):
	res = dfs_help(graph, start_node, visited)

	for vnode in visited:
		if is_edge_node(vnode, graph_size):
			#print(f'vnode {vnode.x},{vnode.y} is an edge node')
			return set()
	return visited

def create_graph(plot, plot_size):
	# List of lists of nodes
	graph = []

	for i,row in enumerate(plot):
		nrow = []
		for j,cell in enumerate(row):
			mnode = Node(i, j, cell)

			# Create node neighbors
			for k in range(i-1, i+2):
				for l in range(j-1, j+2):
					if k == i and l == j:
						continue

					if k >= 0 and k < plot_size and l >= 0 and l < plot_size:
						mnode.neighbors.add((k,l))
			nrow.append(mnode)

		graph.append(nrow)

	return graph

def print_plot(plot):
	for i in plot:
		for j in i:
			print(j,end=' ')
		print()
	print()

def run_sim(graph, graph_size, print_replacements=False):
	visited = set()

	# For each cell in the graph, start iterating over neighbors
	# if the neighbor is a 'valid' neighbor (land tile)
	for row in graph:
		for cell in row:
			lvisited = set()

			# If the tile is a potential island tile, start walking through it
			if cell not in visited and not is_edge_node(cell, graph_size):
				# local visited set will change to 'set()' if it contains an edge node
				lvisited = dfs(graph, graph_size, cell, lvisited)

			# For each of the visited nodes, change their value appropriately
			# (remove islands)
			for l in lvisited:
				if l.value == "#":
					l.value = "*" if print_replacements else "."
				visited.add(l)

def main():
	plot = [
		[".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
		[".", "#", ".", ".", ".", ".", ".", ".", ".", "."],
		[".", "#", ".", ".", ".", ".", ".", ".", ".", "."],
		[".", "#", ".", ".", ".", ".", ".", ".", ".", "."],
		[".", "#", "#", ".", ".", ".", ".", ".", ".", "."],
		[".", ".", ".", ".", "#", "#", ".", ".", ".", "."],
		[".", ".", ".", ".", "#", ".", ".", ".", ".", "."],
		[".", "#", ".", ".", "#", ".", ".", ".", ".", "."],
		["#", "#", ".", ".", ".", ".", ".", ".", ".", "."],
		["#", ".", ".", ".", ".", ".", ".", ".", ".", "."]
	]

	graph_size = 10
	graph = create_graph(plot, graph_size)

	print_plot(plot)
	run_sim(graph, graph_size)

	# Print the map after island removal
	print_plot([[cell.value for cell in row] for row in graph])

if __name__ == "__main__":
	main()
