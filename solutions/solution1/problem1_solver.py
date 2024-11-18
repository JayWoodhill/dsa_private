def largest_contiguous_block(grid):
    # dimensions
    rows = len(grid)
    cols = len(grid[0])

    # track visits
    visited = [[False] * cols for _ in range(rows)]

    from collections import deque

    def bfs(x, y, color):
        # queue
        queue = deque()
        queue.append((x, y))
        visited[x][y] = True
        size = 1

        while queue:
            x, y = queue.popleft()

            # lollipop
            for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                nx, ny = x + dx, y + dy

                # check bounds and visits
                if 0 <= nx < rows and 0 <= ny < cols:
                    if not visited[nx][ny] and grid[nx][ny] == color:
                        visited[nx][ny] = True
                        size += 1
                        queue.append((nx, ny))
        return size

    max_size = 0

    # grid iteration
    for i in range(rows):
        for j in range(cols):
            if not visited[i][j]:
                max_size = max(max_size, bfs(i, j, grid[i][j]))

    return max_size

# input

grid = [
    [1, 1, 1, 1, 2, 2, 2],
    [1, 1, 1, 1, 2, 2, 2],
    [3, 3, 3, 3, 3, 2, 2],
    [3, 3, 3, 3, 3, 2, 2],
    [4, 4, 4, 4, 4, 4, 4],
]

# check
output = largest_contiguous_block(grid)
print(f"output: {output}")
