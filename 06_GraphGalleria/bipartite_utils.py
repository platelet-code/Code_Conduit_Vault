def bipartite_check(n: int, edges: List[Tuple[int, int]]) -> bool:
    graph = [[] for _ in range(n + 1)]
    color = [0] * (n + 1)

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    def bfs(start: int) -> bool:
        queue = deque([start])
        color[start] = 1
        while queue:
            node = queue.popleft()
            next_color = 1 if color[node] == 2 else 2
            for neighbor in graph[node]:
                if color[neighbor] == 0:
                    color[neighbor] = next_color
                    queue.append(neighbor)
                elif color[neighbor] == color[node]:
                    return False
        return True

    return all(bfs(i) if color[i] == 0 else True for i in range(1, n + 1))


def kuhn_munkres(n1: int, n2: int, edges: List[Tuple[int, int]]) -> int:
    match = [-1] * (n2 + 1)
    used = [False] * (n2 + 1)

    def try_match(u: int) -> bool:
        for v in adj[u]:
            if not used[v]:
                used[v] = True
                if match[v] == -1 or try_match(match[v]):
                    match[v] = u
                    return True
        return False

    adj = [[] for _ in range(n1 + 1)]
    for u, v in edges:
        adj[u].append(v)

    result = 0
    for u in range(1, n1 + 1):
        used = [False] * (n2 + 1)
        if try_match(u):
            result += 1

    return result


def hopcroft_karp(n1: int, n2: int, edges: List[Tuple[int, int]]) -> int:
    adj = [[] for _ in range(n1 + 1)]
    pair_u = [-1] * (n1 + 1)
    pair_v = [-1] * (n2 + 1)
    dist = [-1] * (n1 + 1)

    for u, v in edges:
        adj[u].append(v)

    def bfs() -> bool:
        queue = deque([u for u in range(1, n1 + 1) if pair_u[u] == -1])
        for u in range(1, n1 + 1):
            dist[u] = 0 if pair_u[u] == -1 else -1
        found = False
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                if pair_v[v] == -1:
                    found = True
                elif dist[pair_v[v]] == -1:
                    dist[pair_v[v]] = dist[u] + 1
                    queue.append(pair_v[v])
        return found

    def dfs(u: int) -> bool:
        for v in adj[u]:
            if pair_v[v] == -1 or (dist[pair_v[v]] == dist[u] + 1 and dfs(pair_v[v])):
                pair_u[u] = v
                pair_v[v] = u
                return True
        return False

    matching = 0
    while bfs():
        matching += sum(1 for u in range(1, n1 + 1) if pair_u[u] == -1 and dfs(u))
    return matching
