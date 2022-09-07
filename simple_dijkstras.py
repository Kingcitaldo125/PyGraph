from collections import defaultdict

def update_distance(current_node_distance, neighbor):
    msum = current_node_distance + neighbor[0]
    neigh_dist = neighbor[2]

    if msum < neigh_dist:
        nname = neighbor[1]

        # Update neighbor distance
        neighbor[2] = msum
        new_dist = neighbor[2]

        print(f"Updated neighbor '{nname}' distance from '{neigh_dist}' to '{new_dist}'")

def dijkstras(graph, start_node, end_node):
    mqueue = [] # TBD: Update to use a priority queue/heap
    visited = set([graph[start_node][0][1]])
    path = []

    mqueue.insert(0, graph[start_node][0])

    # Dijkstra's algorithm process:
    # 1. Set the starting node's distance to '0', and all others to 'infinity'
    # 2. Update all neighboring nodes' distance values to the sum of the current node's distance + the neighbor's distance
    #    Only do this if the neighbor's distance is greater than the sum of the current node distance & the neighbor's val
    # 3. Determine which edge, leading to 1 or more neighbors, had the lowest 'weight'
    # 4. Visit the neighbor with the lowest edge weight associated with it
    # 5. Repeat, starting at step 2
    while len(mqueue) > 0:
        itm = mqueue.pop()
        weight, name, distance = itm[0], itm[1], itm[2]

        print(f'Visited {name}')

        path.append(name)

        # If the current node is our target/end node,
        # return the path to that target node
        if name == end_node:
            return path

        smallest_weight = 9999

        # Update the distance of the neighbors:
        # Take the sum of the edge's weight and the neighbor's distance;
        # If the sum is less than the neighbor's distance, update the distance
        for neighbor in graph[name]:
            nweight, nname, ndistance = neighbor[0], neighbor[1], neighbor[2]

            update_distance(distance, neighbor)

            # Find the edge leading out of the current node with the smallest weight
            # Only consider edges that lead to nodes we haven't visited yet
            if nname not in visited:
                smallest_weight = min(nweight, smallest_weight)

        # For each of the neighbors, determine which neighbor
        # had the edge with the smallest weight
        # Visit the neighbor with the lowest edge weight associated with it
        for neighbor in graph[name]:
            nweight, nname, ndistance = neighbor[0], neighbor[1], neighbor[2]

            if nname not in visited and nweight <= smallest_weight:
                visited.add(nname)
                mqueue.insert(0, neighbor)

    return []

mgraph = defaultdict(list)

mgraph['0'].append([-1, 'a', 0])

mgraph['a'].append([3, 'b', 9999])
mgraph['a'].append([8, 'c', 9999])
mgraph['b'].append([1, 'd', 9999])
mgraph['b'].append([2, 'e', 9999])
mgraph['c'].append([1, 'd', 9999])
mgraph['c'].append([2, 'f', 9999])
mgraph['d'].append([1, 'b', 9999])
mgraph['d'].append([1, 'c', 9999])
mgraph['d'].append([5, 'f', 9999])

path = dijkstras(mgraph, '0', 'f')

print('path:', path) # a -> b -> d -> c -> f
