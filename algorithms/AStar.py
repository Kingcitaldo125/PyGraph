# Resources:
# https://en.wikipedia.org/wiki/A*_search_algorithm
# https://www.geeksforgeeks.org/a-search-algorithm/

import math

class Node:
	def __init__(self, x, y, name):
		self.x = x
		self.y = y
		self.name = name
		self.parent = None
		self.neighbors = set()
		self.h = 0
		self.g = 0
		self.f = 0

	def __str__(self):
		return self.name

def print_grid(mgrid):
	for row in mgrid:
		for cell in row:
			print(f'Item: {cell}', end=' ')
			print(f'Item Neighbors:',end=' ')
			for n in cell.neighbors:
				print(n,end=' ')
			print()

def get_node_distance(a: Node, b: Node):
	# Pythagoras theorem
	return int(math.sqrt(a.x**2 + b.x**2))

def AStar(start_node: Node, goal_node: Node):
	open = set([start_node])
	closed = set()

	while len(open) > 0:
		least = 99999
		for item in open:
			least = min(least, item.f)

		q = None

		for item in open:
			if item.f == least:
				q = item
				open.remove(item)
				break

		if not q:
			print('Error retrieving smallest heuristic node')
			return

		print(f'Q node: {q}')
		closed.add(q)

		# Update the neighbors' heuristic values
		smallest_neighbor = None
		smallest_neighbor_val = 99999
		for n in q.neighbors:
			if n == goal_node:
				return

			# Calculate G
			n.g = q.g + get_node_distance(q, n)
			if n.g < smallest_neighbor_val:
				smallest_neighbor_val = n.g
				smallest_neighbor = n
				print(f'Smallest Neighbor: {smallest_neighbor}')

			# Calculate H
			n.h = q.g + get_node_distance(q, goal_node)

			# Calculate F
			n.f = n.g + n.h

		# See which neighbor was the smallest neighbor
		# Add that neighbor to the open set
		for n in q.neighbors:
			if n not in open and n not in closed:
				if n == smallest_neighbor:
					n.parent = q
					print(f'Adding {n} to open set')
					open.add(n)

def generate_grid(mgrid: list, width: int, height: int):
	for i in range(width):
		mrow = []

		for j in range(height):
			name = str(i)+','+str(j)
			mnode = Node(i, j, name)
			mrow.append(mnode)

		mgrid.append(mrow)

	# Determine neighbors
	for row in mgrid:
		for cell in row:
			for i in range(cell.x-1, cell.x+2):
				for j in range(cell.y-1, cell.y+2):

					# Skip over the cell in question
					if cell.x == i and cell.y == j:
						continue

					if i >= 0 and i < width and j >= 0 and j < width:
						cell.neighbors.add(mgrid[i][j])

mgrid = []

sq_size = 25

generate_grid(mgrid, sq_size, sq_size)

AStar(mgrid[0][0], mgrid[20][11])
