def dijkstra(n: int, edges: List[Tuple[int, int, int]]) -> int:
    graph = [[float('inf')] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        graph[i][i] = 0
    for u, v, w in edges:
        graph[u][v] = min(graph[u][v], w)
    
    dist = [float('inf')] * (n + 1)
    visited = [False] * (n + 1)
    dist[1] = 0
    
    for _ in range(1, n):
        x = 0
        for i in range(1, n + 1):
            if not visited[i] and (x == 0 or dist[i] < dist[x]):
                x = i
        visited[x] = True
        
        for y in range(1, n + 1):
            dist[y] = min(dist[y], dist[x] + graph[x][y])
    
    return dist[n] if dist[n] != float('inf') else -1


def dijkstra(n: int, edges: List[Tuple[int, int, int]]) -> int:
    graph = [[] for _ in range(n + 1)]
    for u, v, w in edges:
        graph[u].append((v, w))
    
    dist = [float('inf')] * (n + 1)
    dist[1] = 0
    pq = [(0, 1)]

    while pq:
        d, node = heapq.heappop(pq)
        if node == n:
            return d
        if d > dist[node]:
            continue
        for neighbor, weight in graph[node]:
            new_dist = d + weight
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))
    
    return -1


def spfa(n: int, edges: List[Tuple[int, int, int]]) -> Union[str, int]:
    adj_list = [[] for _ in range(n + 1)]
    dist = [float('inf')] * (n + 1)
    in_queue = [False] * (n + 1)

    for x, y, z in edges:
        adj_list[x].append((y, z))

    queue = deque([1])
    dist[1] = 0
    in_queue[1] = True

    while queue:
        x = queue.popleft()
        in_queue[x] = False
        for y, z in adj_list[x]:
            if dist[y] > dist[x] + z:
                dist[y] = dist[x] + z
                if not in_queue[y]:
                    queue.append(y)
                    in_queue[y] = True

    return dist[n] if dist[n] != float('inf') else "impossible"


def floyd_warshall(n: int, edges: List[Tuple[int, int, int]]) -> List[List[int]]:
    dist = [[float('inf')] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        dist[i][i] = 0

    for x, y, z in edges:
        dist[x][y] = min(dist[x][y], z)

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist


def bellman_ford(n: int, max_iterations: int, edges: List[Tuple[int, int, int]]) -> Union[str, int]:
    dist = [float('inf')] * (num_vertices + 1)
    dist[1] = 0

    for _ in range(max_iterations):
        new_dist = dist[:]
        for x, y, z in edges:
            dist[y] = min(dist[y], new_dist[x] + z)

    return dist[n] if dist[n] != float('inf') else "impossible"


def has_negative_cycle(n: int, edges: List[Tuple[int, int, int]]) -> bool:
    adj = [[] for _ in range(n + 1)]
    dist = [float('inf')] * (n + 1)
    cnt = [0] * (n + 1)
    vis = [False] * (n + 1)

    for x, y, z in edges:
        adj[x].append((y, z))

    queue = deque(range(1, n + 1))
    for i in range(1, n + 1):
        dist[i] = 0
        vis[i] = True

    while queue:
        x = queue.popleft()
        vis[x] = False
        for y, z in adj[x]:
            if dist[y] > dist[x] + z:
                dist[y] = dist[x] + z
                cnt[y] = cnt[x] + 1
                if cnt[y] >= n:
                    return True
                if not vis[y]:
                    queue.append(y)
                    vis[y] = True

    return False
