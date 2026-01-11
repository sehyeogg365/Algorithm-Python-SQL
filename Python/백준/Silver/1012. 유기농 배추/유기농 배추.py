import sys
sys.setrecursionlimit(100000)  # 더 큰 값으로 설정

def dfs(x, y, m, n, graph):
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    
    graph[y][x] = 0
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if (0 <= nx < m) and (0 <= ny < n):
            if graph[ny][nx] == 1:
                dfs(nx, ny, m, n, graph)

t = int(sys.stdin.readline())
for _ in range(t):
    m, n, k = map(int, sys.stdin.readline().split())
    graph = [[0] * m for _ in range(n)]
    count = 0
    
    for _ in range(k):
        a, b = map(int, sys.stdin.readline().split())
        graph[b][a] = 1
        
    for i in range(m):
        for j in range(n):
            if graph[j][i] == 1:
                dfs(i, j, m, n, graph)
                count += 1
                
    print(count)