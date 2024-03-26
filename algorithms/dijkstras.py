def dijkstras(graph, start_node):
	mq = []
	visited = set([])
	paths = {}

	mq.append((0, start_node))
	visited.add(start_node)

	while len(mq) > 0:
		node_id = mq[0][1]
		node_weight = mq[0][0]

		mq.pop(0)

		print(f"Visited {node_id}")

		min_neighbor_node = ''
		min_neighbor_val = 999999
		for neighbor in graph[node_id][1:]:
			graph[neighbor[1]][0] = min(graph[neighbor[1]][0], node_weight + neighbor[0])

			paths[neighbor[1]] = graph[neighbor[1]][0]

			if neighbor[1] not in visited and graph[neighbor[1]][0] < min_neighbor_val:
				min_neighbor_val = graph[neighbor[1]][0]
				min_neighbor_node = neighbor[1]

			if min_neighbor_node not in visited and min_neighbor_node != '':
				visited.add(min_neighbor_node)
				mq.append((min_neighbor_val, min_neighbor_node))

	return paths

graph = {}

graph['A'] = [0, [3, 'B'], [4, 'C']]
graph['B'] = [999999, [1, 'A'], [1, 'C']]
graph['C'] = [999999, [4, 'A'], [1, 'B'], [3, 'D']]
graph['D'] = [999999, [3, 'C']]

print(dijkstras(graph, "A"))
