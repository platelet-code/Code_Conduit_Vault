def prim_basic(n: int, edges: List[Tuple[int, int, int]]) -> Union[str, int]:
    g = [[float('inf')] * (n + 1) for _ in range(n + 1)]
    for x, y, z in edges:
        g[x][y] = g[y][x] = min(g[x][y], z)

    dist = [float('inf')] * (n + 1)
    dist[1] = 0
    vis = [False] * (n + 1)
    total_cost = 0

    for _ in range(n):
        x = min((dist[i], i) for i in range(1, n + 1) if not vis[i])[1]
        
        if dist[x] == float('inf'):
            return "impossible"
        
        vis[x] = True
        total_cost += dist[x]
        
        for y in range(1, n + 1):
            dist[y] = min(g[x][y], dist[y])
    
    return total_cost


def prim_optimized(n: int, edges: List[Tuple[int, int, int]]) -> Union[str, int]:
    g = [[float('inf')] * (n + 1) for _ in range(n + 1)]
    for x, y, z in edges:
        g[x][y] = g[y][x] = min(g[x][y], z)

    dist = [float('inf')] * (n + 1)
    dist[1] = 0
    visited = [False] * (n + 1)
    min_heap = [(0, 1)]
    total_cost = 0

    while min_heap:
        cost, x = heapq.heappop(min_heap)
        
        if visited[x]:
            continue
        
        visited[x] = True
        total_cost += cost

        for y in range(1, n + 1):
            if not visited[y] and g[x][y] < dist[y]:
                dist[y] = g[x][y]
                heapq.heappush(min_heap, (dist[y], y))

    return total_cost if all(visited[1:]) else "impossible"


def kruskal(n: int, edges: List[Tuple[int, int, int]]) -> Union[int, str]:
    parent = list(range(n + 1))
    def find(x: int) -> int:
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    edges.sort(key=lambda x: x[2])
    mst_cost = 0
    edges_used = 0
    
    for x, y, z in edges:
        root_x, root_y = find(x), find(y)
        if root_x != root_y:
            parent[root_x] = root_y
            mst_cost += z
            edges_used += 1
            if edges_used == n - 1:
                break
    
    return mst_cost if edges_used == n - 1 else "impossible"
