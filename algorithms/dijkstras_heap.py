import heapq

from collections import defaultdict

def dijkstras_heap(graph, start, target):
    mq = [(0, start)]
    visited = set()

    while len(mq) > 0:
        cost, node = heapq.heappop(mq)
        visited.add(node)

        if node == target:
            return cost

        for neigh in graph[node]:
            neigh_cost, neigh_name = neigh[0], neigh[1]

            if neigh_name not in visited:
                heapq.heappush(mq, (neigh_cost + cost, neigh_name))

    return -1

graph = defaultdict(list)

graph['A'].append((4, 'B'))
graph['A'].append((2, 'C'))

graph['B'].append((3, 'C'))
graph['B'].append((2, 'D'))
graph['B'].append((3, 'E'))

graph['C'].append((1, 'B'))
graph['C'].append((4, 'D'))
graph['C'].append((5, 'E'))

# Needed for indexing the neighbors of 'B', 'C', and 'E'
graph['D']

graph['E'].append((1, 'D'))

#mc = dijkstras_heap(graph, 'A', 'B') # 3
#mc = dijkstras_heap(graph, 'A', 'C') # 2
#mc = dijkstras_heap(graph, 'A', 'D') # 5
mc = dijkstras_heap(graph, 'A', 'E') # 6

print(f'{mc}')
