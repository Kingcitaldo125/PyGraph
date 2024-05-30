# https://en.wikipedia.org/wiki/Moore_neighborhood
# https://en.wikipedia.org/wiki/Von_Neumann_neighborhood

def get_moore_neighborhood(matrix, x, y):
    row_length = len(matrix[0])
    col_length = len(matrix)
    neighbors = []

    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            if i < 0 or i >= row_length or j < 0 or j >= col_length:
                continue
            if i == x and j == y:
                continue
            neighbors.append((i, j))
    return neighbors


def get_von_neumann_neighborhood(matrix, x, y):
    row_length = len(matrix[0])
    col_length = len(matrix)
    neighbors = []

    for i in range(x - 1, x + 2):
        if i < 0 or i >= row_length:
            continue
        if i == x:
            continue
        neighbors.append((i, y))
    for i in range(y - 1, y + 2):
        if i < 0 or i >= col_length:
            continue
        if i == y:
            continue
        neighbors.append((x, i))
    return neighbors

