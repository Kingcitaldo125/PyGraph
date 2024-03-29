import graphviz

from time import time

from Graph.Graph import Graph

def render_graph(graph, view=True):
	dot = graphviz.Digraph(comment='My Graph')

	for k,v in graph.adj_list.items():
		dot.node(k)
		for vv in v:
			dot.edge(k,vv)

	dot.render('doctest-output/graph.gv', view=view)

def measure_time(func, node1, node2):
	before = time()
	res = func(node1, node2)
	now = time()
	print(func.__name__, node1, "->", node2, ":", res)
	return now-before

graph = Graph(directed=True)

nodes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

for n in nodes:
	graph.add_node(n)

graph.add_edge("A", "B")
graph.add_edge("A", "C")
graph.add_edge("A", "D")
graph.add_edge("B", "E")
graph.add_edge("C", "F")
graph.add_edge("D", "G")

graph.add_edge("B", "H")
graph.add_edge("C", "I")
graph.add_edge("D", "J")

print(graph)
#render_graph(graph)

#print(graph.hasPathBFS("A", "F"))
#print(graph.hasPathDFS("A", "F"))

#print(graph.hasPathBFS("A", "G"))
#print(graph.hasPathDFS("A", "G"))

'''
bfs_time = measure_time(graph.hasPathBFS, "A", "G")
dfs_time = measure_time(graph.hasPathDFS, "A", "G")

print("bfs_time", bfs_time)
print("dfs_time", dfs_time)
'''
