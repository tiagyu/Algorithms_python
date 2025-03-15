from collections import deque

def bfs_maze(maze):
    n, m = len(maze), len(maze[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    queue = deque([(0, 0)])
    distance = [[0] * m for _ in range(n)]
    distance[0][0] = 1 

    while queue:
        x, y = queue.popleft()
        
        if x == n - 1 and y == m - 1:
            return distance[x][y]
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] == 1 and distance[nx][ny] == 0:
                distance[nx][ny] = distance[x][y] + 1
                queue.append((nx, ny))

maze = [
    [1, 1, 1, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 1, 1, 1, 1]
]
print(bfs_maze(maze))